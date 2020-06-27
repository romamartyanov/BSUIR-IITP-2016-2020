.model small
.386
.stack 200h



.data
    id dw 0
    minus dw 0
    temp_num dw 0

    minus_symbal db 13,10,'-$'
    not_a_number db 13, 10, 'Try again ' ,10, '$'                 ; переменные, которые содержать сообщения
    out_of_range db 13, 10, 'STOP ' , 10, '$'                     ; db 13, 10 код инструкций для перехода на новую строку
    zero_dividing db 13, 10, 'Zero dividing ' , 10, '$'           ;

    backspace db 27, '[K$'                                        ; переменная, содержащая пустой символ
    escape db 13, 27, '[K$'                                       ;


.code
scanning_cmd proc           ; заносим регистры в стек
    push ax
    push cx
    push dx
    mov cx, 10              ; регистр, нужеый для деления на 10
    xor bx, bx

minus_entering:
    mov ah, 1               ; использование клавиатуры для ввода
    int 21h                 ;

    cmp al, '-'	            ; если минус, то устанавливаем признак минуса
    jnz entering_cycle_no_minus

    mov minus, 1
    jmp entering_cycle

entering_cycle:
    mov ah, 1               ; использование клавиатуры для ввода
    int 21h                 ;

entering_cycle_no_minus:
    cmp al, 13              ; код символа 'enter'
    je enter_checking       ; если 'enter', то перехоидим к к моменту, где процедура заканчивается

    cmp al, 8                        ; сравнение с символом backspace
    je backspace_entered             ;

    cmp al, 27                       ; сравнение с символом escape
    je escape_entered                ;

    cmp al, '9'                      ; код введенного больше, чем код символа 9
    ja not_a_number_detected         ;

    cmp al, '0'                      ; код введенного меньше, чем код символа 0
    jb not_a_number_detected

    sub al, '0'                      ; перевод из ASCII в число
    xor ah, ah

    xchg ax, bx                      ; меняем местами ax и bx
    mul cx                           ; ax = ax * 10
    jc out_of_range_exception        ; если в ax переполнение

    add ax, bx                       ;
    jc out_of_range_exception        ; если ax = ax + bx переполнение

    mov temp_num, ax
    cmp minus, 1
    je minus_range
    ;jc out_of_range_exception
    jne plus_range

minus_range:
    sub ax, 1
    mov cx, 2
    mul cx

    jc out_of_range_exception

    mov cx, 10
    mov ax, temp_num

    mov bx, ax
    jmp entering_cycle

plus_range:
    mov cx, 2
    mul cx

    jc out_of_range_exception

    mov cx, 10
    mov ax, temp_num

    mov bx, ax
    jmp entering_cycle


backspace_entered:                   ; обработка введенного backspace
    xor dx, dx                       ; очиста dx

    mov ax, bx                       ; очистка строки на один символ
    div cx                           ; путем деления на 10 (остаток это последний символ)

    mov bx, ax
    mov ah, 9                        ; функция вывода сообщения на экран
    mov dx, offset backspace         ;

    int 21h
    jmp entering_cycle


escape_entered:                      ; почти тоже самое, что и в backspace_entered
    xor ax, ax
    xor bx, bx

    mov ah, 9                        ; но без удаления символа
    mov dx, offset escape            ;

    mov minus, 0

    int 21h
    jmp entering_cycle


not_a_number_detected:              ; вывод сообщения, если введено не число
    mov ah, 9                       ; функция вывода сообщения на экран
    mov dx, offset not_a_number     ;

    mov minus, 0

    int 21h
    jmp main


out_of_range_exception:            ; если переполнение
    xor ah, ah

    xor ax, ax                     ; очистка регистров
    xor bx, bx                     ;
    mov minus, 0

    mov ah, 9
    mov dx, offset out_of_range    ; выводим сообщение
    int 21h
    jmp entering_cycle             ; начинаем вводить заново

zero_dividing_exception:
    mov ah, 9                      ; функция вывода сообщения на экран
    mov dx, offset zero_dividing   ; вывод на экран сообщения

    int 21h
    jmp main


enter_checking:                    ; отработка введеного enter
    cmp minus, 1	                 ; если установлен признак отрицательного числа
	  je negativing_bx

    jmp ending_scaning_proc


negativing_bx:
    ;neg bx		                     ; то меняем знак
    inc id

    jmp ending_scaning_proc


ending_scaning_proc:
    pop dx
    pop cx                         ; pop извлекает значение из стека, т.е. извлекает значение из ячейки памяти
    pop ax                         ;

    mov minus, 0

    ret
scanning_cmd endp


print_awnser proc                  ; процедура вывода результата деления на экран
    push ax                        ; обратно заносим значения регистров в стек
    push bx                        ;
    push cx                        ;
    push dx                        ;

    xor cx, cx                     ; очищаем регистр, в котором хранилось 10, необходимое для деления
    mov bx, 10


printing_cycle:                    ; вывод ответа на экран
    xor dx, dx

    div bx                         ; ax = ax / 10
    push dx                        ; в стек заносится 0

    inc cx                         ; счетчик кол-ва цифр для инструкции loop
    test ax, ax                    ; равен ли регистр нулю
    jne printing_cycle             ; если нет, то цикл продолжается

    cmp id, 1
    je minus_output
    jmp printing


  minus_output:                    ; вывод минуса
    mov ah, 9
    lea dx, minus_symbal

    int 21h
    jmp printing


printing:                          ; если да, то заходим сюда
    mov ah, 02h                    ; иструкция вывода на экран из регистра
    xor dx, dx

    pop dx

    add dl, '0'                    ; инструкция для вывода числе на экран

    int 21h
    loop printing                  ; цикл зависит от значения регистра cx

    jmp exit
    ret
print_awnser endp


main:
    mov ax, @data
    mov ds, ax
    xor bx, bx                      ; очистка регистров
    xor ax, ax                      ;
    xor al, al                      ;

    call scanning_cmd               ; вводим первое число

    mov ax, bx                      ; заносим его в ax
    call scanning_cmd               ; вводим второе число

    or bx, bx                       ; поверка введеного второго числа на 0
    je zero_dividing_exception      ;

    xor dx, dx                      ; очистка регистра dx

    cwd
    idiv bx                          ; деление ax на bx

    cmp id, 1
    je check_minus


continue:
    call print_awnser               ; вызываем процедуру вывода ответа на экран
    jmp exit                        ; переходим к выходу из программы


check_minus:
    ; neg ax
    jmp continue


exit:
    mov ah, 4ch
    int 21h
    end main


End
