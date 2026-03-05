package com.jpmc.transaction.dto;

import lombok.Data;
import java.math.BigDecimal;

@Data
public class TransactionMessage {
    private String transactionId;
    private Long userId;
    private BigDecimal amount;
    private String type;
}
