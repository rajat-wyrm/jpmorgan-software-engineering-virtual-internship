package com.jpmc.transaction.config;

import com.jpmc.transaction.model.User;
import com.jpmc.transaction.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import java.math.BigDecimal;

@Configuration
@RequiredArgsConstructor
@Slf4j
public class DataInitializer {
    
    private final UserRepository userRepository;
    
    @Bean
    public CommandLineRunner initializeData() {
        return args -> {
            log.info("Initializing test data...");
            
            if (userRepository.count() == 0) {
                // Create test users
                User user1 = new User();
                user1.setUsername("john.doe");
                user1.setEmail("john.doe@example.com");
                user1.setBalance(new BigDecimal("1000.00"));
                userRepository.save(user1);
                
                User user2 = new User();
                user2.setUsername("jane.smith");
                user2.setEmail("jane.smith@example.com");
                user2.setBalance(new BigDecimal("2500.00"));
                userRepository.save(user2);
                
                log.info("Created 2 test users");
            }
        };
    }
}
