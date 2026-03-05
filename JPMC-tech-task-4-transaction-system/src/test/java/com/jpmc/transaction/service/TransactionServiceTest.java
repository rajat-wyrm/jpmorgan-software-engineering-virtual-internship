package com.jpmc.transaction.service;

import com.jpmc.transaction.dto.IncentiveResponse;
import com.jpmc.transaction.dto.TransactionMessage;
import com.jpmc.transaction.model.Transaction;
import com.jpmc.transaction.model.User;
import com.jpmc.transaction.repository.TransactionRepository;
import com.jpmc.transaction.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.web.client.RestTemplate;
import java.math.BigDecimal;
import java.util.Optional;
import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class TransactionServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private TransactionRepository transactionRepository;
    
    @Mock
    private RestTemplate restTemplate;
    
    @InjectMocks
    private TransactionService transactionService;
    
    private User testUser;
    private TransactionMessage testMessage;
    
    @BeforeEach
    void setUp() {
        testUser = new User();
        testUser.setId(1L);
        testUser.setUsername("testuser");
        testUser.setEmail("test@example.com");
        testUser.setBalance(new BigDecimal("1000.00"));
        
        testMessage = new TransactionMessage();
        testMessage.setTransactionId("tx-123");
        testMessage.setUserId(1L);
        testMessage.setAmount(new BigDecimal("50.00"));
        testMessage.setType("DEPOSIT");
    }
    
    @Test
    void testProcessTransaction_Success() {
        when(userRepository.findById(1L)).thenReturn(Optional.of(testUser));
        when(transactionRepository.save(any(Transaction.class)))
                .thenAnswer(i -> i.getArgument(0));
        when(restTemplate.postForObject(any(), any(), any()))
                .thenReturn(new IncentiveResponse(new BigDecimal("5.00")));
        
        Transaction result = transactionService.processTransaction(testMessage);
        
        assertThat(result).isNotNull();
        assertThat(result.getStatus()).isEqualTo("COMPLETED");
        assertThat(result.getIncentiveAmount()).isEqualTo(new BigDecimal("5.00"));
    }
    
    @Test
    void testProcessTransaction_UserNotFound() {
        when(userRepository.findById(1L)).thenReturn(Optional.empty());
        
        assertThatThrownBy(() -> transactionService.processTransaction(testMessage))
                .isInstanceOf(RuntimeException.class)
                .hasMessageContaining("User not found");
    }
    
    @Test
    void testProcessTransaction_InvalidAmount() {
        testMessage.setAmount(new BigDecimal("-10.00"));
        when(userRepository.findById(1L)).thenReturn(Optional.of(testUser));
        
        assertThatThrownBy(() -> transactionService.processTransaction(testMessage))
                .isInstanceOf(RuntimeException.class)
                .hasMessageContaining("Invalid transaction");
    }
    
    @Test
    void testGetUserBalance() {
        when(userRepository.findBalanceById(1L)).thenReturn(new BigDecimal("1000.00"));
        
        BigDecimal balance = transactionService.getUserBalance(1L);
        
        assertThat(balance).isEqualTo(new BigDecimal("1000.00"));
    }
}
