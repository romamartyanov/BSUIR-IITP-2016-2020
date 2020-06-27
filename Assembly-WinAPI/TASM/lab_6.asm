model tiny

.code
.386

org 100h

start:
  mov si, 80h                             ; Разбор аргументов запуска программы (80h отвечает за длину)
  lodsb
  cmp al, 0                               ; Длинна параметра равна 0 ()
  je set_old_handler                      ; Идем на стандартный обработчик

  cmp al, 3                               ;
  jne param_input_error                   ; Обработка неправильного параметра (!= 3)

  mov cx, 3
  mov di, offset param                    ; Сам параметр
  repe cmpsb
  jne param_input_error                   ; Тоже обработчик ошибки параметра, если параметр не занесен

  call remove_old_handler                 ; Удаояем старый обработчик
  mov ah, 4ch
  int 21h

check_handler_installed proc
  push ax bx es si

  xor ax, ax
  mov es, ax

  mov si, word ptr es:[09h * 4]            ; Берем адрес обработчика
  mov bx, word ptr es:[09h * 4 + 2]        ; и его сегмент

  mov es, bx
  cmp word ptr es:[si + 10], 4242h        ; сравниваем стандартный обработчик с

  jne good

  bad:
    mov ah, 09h

    mov dx, offset handler_already_installed      ; если обработчик уже заменен

    int 21h
    mov ah, 4ch
    int 21h

  good:
    mov ax, cs
    mov es, ax

    mov ax, offset interrupt_flag                  ; заносим свой обработчик

    pop si es bx ax
    ret
check_handler_installed endp

set_old_handler:
  push ax es
  call check_handler_installed

  xor ax, ax
  mov es, ax

  mov ax, word ptr es:[09h * 4]                   ;
  mov word ptr old_handler, ax                    ; адреса старого обработчика
  mov ax, word ptr es:[09h * 4 + 2]               ;
  mov word ptr old_handler + 2, ax                ;

  mov ax, cs                                      ;
  mov word ptr es:[09h * 4 + 2], ax               ;
  mov ax, offset new_handler                      ; ставим новый обработчик
  mov word ptr es:[09h * 4], ax                   ;

  pop es ax                                       ;
  mov ah, 09h                                     ;
  mov dx, offset good_inst                        ; новый обработчик успешно установлен

  int 21h                                         ;
  mov dx, offset last_byte                        ;
  int 27h                                         ; отправляемся к выходу

  ret

param_input_error:                                ;
  mov ah, 09h                                     ;
  mov dx, offset inp_err                          ; введен неправильный параметр
  int 21h                                         ;
  mov ah, 4ch                                     ;
  int 21h                                         ;
  ret

remove_old_handler proc
  push dx ax bx
  push es
  push si

  call if_handler_detected

  xor ax, ax
  mov es, ax

  mov ax, word ptr es:[09h * 4]                   ; берем адрес нового обработчика
  mov bx, word ptr es:[09h * 4 + 2]               ; и его сегмент
  mov es, bx
  mov si, ax

  mov ax, word ptr es:[si + 2]                    ; берем первое слово по этому адресу (адрес старого обработчика)
  mov bx, word ptr es:[si + 4]                    ; берем второе слово по этому адресу (семент старого обработчика)

  push ax
  mov ax, bx
  pop ax

  push bx                                         ;
  mov bx, 0                                       ; восстанавливаем адрес сегмента
  mov es, bx                                      ;
  pop bx                                          ;

  mov word ptr es:[09h * 4], ax                   ; пушим старый адрес в адрес обработкика
  mov word ptr es:[09h * 4 + 2], bx               ; пушим старый адрес в адрес сегмента обработкика
  mov ah, 09h
  mov dx, offset good_del
  int 21h

  pop si es bx ax dx
  ret
remove_old_handler endp

if_handler_detected proc
  push ax bx
  push es
  push si

  xor ax, ax
  mov es, ax

  mov si, word ptr es:[09h * 4]       ; берем адрес нового обработчика
  mov bx, word ptr es:[09h * 4 + 2]   ; и его сегмент

  mov es, bx
  mov ax, es

  add si, 10
  mov ax, si
  mov ax, word ptr es:[si]

  cmp ax, 4242h                       ; сравнивание с нашим прерыванием
  je good1

  bad1:
    mov ah, 09h                         ;
    mov dx, offset rem_err              ; ошибка обработки прерывания

    int 21h                             ;
    mov ah, 4ch                         ;
    int 21h                             ;


  good1:
    pop si es bx ax
  ret
if_handler_detected endp

new_handler:                            ; прописываем свой обрабочик клавиатуры
  jmp $+12

  old_handler dd 0, 0
  interrupt_flag dw 4242h

  handler_label:
  push es ds
  push si di
  push cx bx dx ax

  xor ax, ax

  in al, 60h

  ; проверка A
  cmp_A:
    cmp al, 1Eh
    jne cmp_E

    push cx
    mov cl, 'e'
    call push_letter_to_buffer

    pop cx
    jmp end_handler

; проверка E
  cmp_E:
    cmp al, 12h
    jne cmp_I

    push cx
    mov cl, 'i'
    call push_letter_to_buffer

    pop cx
    jmp end_handler

  ; проверка I
  cmp_I:
    cmp al, 17h
    jne cmp_O

    push cx
    mov cl, 'o'
    call push_letter_to_buffer

    pop cx
    jmp end_handler

  ; проверка O
  cmp_O:
    cmp al, 18h
    jne cmp_U

    push cx
    mov cl, 'u'
    call push_letter_to_buffer

    pop cx
    jmp end_handler

  ; проверка U
  cmp_U:

    cmp al, 16h
    jne cmp_Y

    push cx
    mov cl, 'y'
    call push_letter_to_buffer

    pop cx
    jmp end_handler

  ; проверка Y
  cmp_Y:

    cmp al, 15h
    jne main_handler

    push cx
    mov cl, 'a'
    call push_letter_to_buffer

    pop cx
    jmp end_handler


end_handler:
  mov al, 20h
  out 20h, al
  pop ax dx bx cx
  pop di si
  pop ds es

  iret

main_handler:
  pop ax dx bx cx
  pop di si
  pop ds es

  jmp dword ptr cs:old_handler
	iret

push_letter_to_buffer proc
  push ax
  push es ds
  push si di
  push bx cx

  mov ax, 0040h
  mov es, ax
  mov di, word ptr es:[001Ah]         ; чтение головы буфера клавиатуры
  mov bx, word ptr es:[001Ch]         ; чтение хвоста буфера клавиатуры

  cmp di, 003ch                       ; если head указывает на конец буфера
  jne g1

  mov di, 001eh

  g1:
    mov al, cl
    mov byte ptr es:[di], al
    add di, 2
    mov word ptr es:[001ch], di       ; установить указатель на конец

  pop cx bx
  pop di si
  pop ds es
  pop ax

  ret
push_letter_to_buffer endp


param db ' -d'

good_inst db 'Interrupt is overloaded', 10, 13, '$'
good_del db 'Handler deleted', 10, 13, '$'

rem_err db 'Error: handler does not exist', 10, 13, '$'
handler_already_installed db 'Error: handler is already installed', 10, 13, '$'
inp_err db 'Error: bad command line parameter', 10, 13, '$'

last_byte:
end Start
