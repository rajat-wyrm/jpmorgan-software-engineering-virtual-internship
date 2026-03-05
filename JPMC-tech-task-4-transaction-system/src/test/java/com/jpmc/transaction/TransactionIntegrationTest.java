package com.jpmc.transaction;

import com.jpmc.transaction.dto.TransactionMessage;
import com.jpmc.transaction.model.User;
import com.jpmc.transaction.repository.UserRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.test.context.ActiveProfiles;
import java.math.BigDecimal;
import java.util.concurrent.TimeUnit;
import static org.assertj.core.api.Assertions.assertThat;
import static org.awaitility.Awaitility.await;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test")
public class TransactionIntegrationTest {
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    @Test
    public void testUserBalanceEndpoint() {
        ResponseEntity<String> response = restTemplate.getForEntity(
                "/api/v1/users/1/balance", String.class);
        assertThat(response.getStatusCode().is2xxSuccessful()).isTrue();
        assertThat(response.getBody()).contains("userId");
    }
    
    @Test
    public void testKafkaTransactionProcessing() {
        // Create test transaction
        TransactionMessage message = new TransactionMessage();
        message.setTransactionId("test-tx-123");
        message.setUserId(1L);
        message.setAmount(new BigDecimal("100.00"));
        message.setType("DEPOSIT");
        
        // Send to Kafka
        kafkaTemplate.send("transactions", message);
        
        // Wait for processing
        await().atMost(5, TimeUnit.SECONDS).untilAsserted(() -> {
            User user = userRepository.findById(1L).orElse(null);
            assertThat(user).isNotNull();
            assertThat(user.getBalance()).isGreaterThan(new BigDecimal("1000.00"));
        });
    }
}
