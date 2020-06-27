model small
.stack 100h

.data
a dw 4     ; a = 4
b dw 5     ; b = 5
c dw 2
e dw 7

temp1 dw ?
temp2 dw ?

.code

start:
  mov AX, @data
  mov DS, AX

  ;mov AX, 0      ; AX = 0
  ;mov BX, 0      ; BX = 0
  ;mov CX, 0

  mov AX, a
  mov BX, b
  and AX, BX       ; a AND b
  mov temp1, AX    ; temp1 = (a AND b)

  mov AX, c         ;
  mul c             ;
  mul c             ;
  mul c             ;
  mov temp2, AX     ; temp2 = c ^ 4

  mov AX, temp1
  mov BX, temp2
  cmp AX, BX        ; if temp1 == temp2:
  jz else0
  jmp else1         ; else:   (temp1 != temp2)
  else0:
     mov AX, c      ;
     div e          ;
     div b          ;
     add AX, a      ;  AX =  с / d / b + a

     jmp last

  else1:
    mov AX, c       ;
    add AX, b       ;
    mov temp1, AX   ; temp1 = c + b

    mov AX, a       ;
    mul a           ;
    mul a           ; AX = a ^ 3

    mov BX, b       ;
    mul b           ;
    mul b           ; BX = b ^ 3

    add AX, BX      ; AX = AX + BX
    mov temp2, AX   ; temp2 = temp2 + AX

    mov AX, temp1
    mov BX, temp2
    cmp AX, BX       ; if temp1 == temp2:
    je else1_0
    jmp else1_1       ; else:   (temp1 != temp2)
    else1_0:
      mov BX, b       ;
      add BX, c       ; BX = b + c

      mov CX, a       ; CX = a
      xor CX, BX      ; CX XOR BX  --> a XOR (b + c)
      mov AX, CX
      jmp last

    else1_1:
      mov AX, c	      ;
      shr AX, 3       ; AX >> 3
      jmp last


  last:
  int 21h
end start
