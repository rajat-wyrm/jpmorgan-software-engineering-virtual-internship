package com.jpmc.transaction.dto;

import lombok.Data;
import java.math.BigDecimal;

@Data
public class BalanceResponse {
    private Long userId;
    private BigDecimal balance;
    private String timestamp;
    
    public BalanceResponse(Long userId, BigDecimal balance) {
        this.userId = userId;
        this.balance = balance;
        this.timestamp = java.time.LocalDateTime.now().toString();
    }
}
