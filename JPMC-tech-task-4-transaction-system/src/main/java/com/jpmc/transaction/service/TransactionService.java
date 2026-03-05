package com.jpmc.transaction.service;

import com.jpmc.transaction.dto.IncentiveResponse;
import com.jpmc.transaction.dto.TransactionMessage;
import com.jpmc.transaction.model.Transaction;
import com.jpmc.transaction.model.User;
import com.jpmc.transaction.repository.TransactionRepository;
import com.jpmc.transaction.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.client.RestTemplate;

import java.math.BigDecimal;

@Service
@RequiredArgsConstructor
@Slf4j
public class TransactionService {
    
    private final UserRepository userRepository;
    private final TransactionRepository transactionRepository;
    private final RestTemplate restTemplate;
    
    @Value("")
    private String incentiveApiUrl;
    
    @Transactional
    public Transaction processTransaction(TransactionMessage message) {
        log.info("Processing transaction: {}", message.getTransactionId());
        
        // Validate user
        User user = userRepository.findById(message.getUserId())
                .orElseThrow(() -> new RuntimeException("User not found"));
        
        // Validate amount
        if (message.getAmount().compareTo(BigDecimal.ZERO) <= 0) {
            throw new RuntimeException("Invalid transaction amount");
        }
        
        // Create transaction
        Transaction transaction = new Transaction();
        transaction.setTransactionId(message.getTransactionId());
        transaction.setUser(user);
        transaction.setAmount(message.getAmount());
        transaction.setType(message.getType());
        transaction.setStatus("PROCESSING");
        
        // Save transaction
        transaction = transactionRepository.save(transaction);
        
        // Get incentive
        try {
            IncentiveResponse incentive = restTemplate.postForObject(
                    incentiveApiUrl,
                    transaction,
                    IncentiveResponse.class
            );
            
            if (incentive != null && incentive.getApplied()) {
                transaction.setIncentiveAmount(incentive.getIncentiveAmount());
                log.info("Incentive applied: {}", incentive.getIncentiveAmount());
            }
        } catch (Exception e) {
            log.warn("Incentive API call failed: {}", e.getMessage());
        }
        
        // Update user balance
        BigDecimal newBalance = user.getBalance().add(transaction.getAmount());
        if (transaction.getIncentiveAmount() != null) {
            newBalance = newBalance.add(transaction.getIncentiveAmount());
        }
        user.setBalance(newBalance);
        userRepository.save(user);
        
        // Complete transaction
        transaction.setStatus("COMPLETED");
        transaction = transactionRepository.save(transaction);
        
        log.info("Transaction completed. New balance: {}", newBalance);
        return transaction;
    }
    
    public BigDecimal getUserBalance(Long userId) {
        return userRepository.findBalanceById(userId);
    }
}
