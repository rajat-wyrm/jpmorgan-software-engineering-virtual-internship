package com.jpmc.transaction.controller;

import com.jpmc.transaction.dto.BalanceResponse;
import com.jpmc.transaction.service.TransactionService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.math.BigDecimal;

@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
public class UserController {
    
    private final TransactionService transactionService;
    
    @GetMapping("/{userId}/balance")
    public ResponseEntity<BalanceResponse> getUserBalance(@PathVariable Long userId) {
        BigDecimal balance = transactionService.getUserBalance(userId);
        return ResponseEntity.ok(new BalanceResponse(userId, balance));
    }
}
