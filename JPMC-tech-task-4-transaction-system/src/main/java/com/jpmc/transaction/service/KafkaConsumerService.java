package com.jpmc.transaction.service;

import com.jpmc.transaction.dto.TransactionMessage;
import com.jpmc.transaction.model.Transaction;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class KafkaConsumerService {
    
    private final TransactionService transactionService;
    
    @KafkaListener(topics = "transactions", groupId = "transaction-group")
    public void consumeTransaction(TransactionMessage message) {
        log.info("Received transaction from Kafka: {}", message.getTransactionId());
        
        try {
            Transaction processed = transactionService.processTransaction(message);
            log.info("Successfully processed transaction: {}", processed.getId());
        } catch (Exception e) {
            log.error("Failed to process transaction: {}", e.getMessage());
        }
    }
}
