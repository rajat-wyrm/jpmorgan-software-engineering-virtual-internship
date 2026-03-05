package com.jpmc.transaction.dto;

import lombok.Data;
import java.math.BigDecimal;

@Data
public class IncentiveResponse {
    private BigDecimal incentiveAmount;
    private String incentiveType;
    private Boolean applied;
    
    public IncentiveResponse() {
        this.incentiveAmount = BigDecimal.ZERO;
        this.applied = false;
    }
    
    public IncentiveResponse(BigDecimal amount) {
        this.incentiveAmount = amount;
        this.applied = amount.compareTo(BigDecimal.ZERO) > 0;
    }
}
