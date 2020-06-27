.model small
.stack 100h

.data
  max_string_length db 255       ; зарезервировать 255 байтов
  min_string_length db 0         ; зарезервировать 0 байтов

  char_massive db 255 dup (0)    ; зарезервировать 255 байтов и поместить туда 0
  string db 255 dup (0)          ;

  input_message db "Enter string: ", 13, 10, "$"

.code
.386


; переход на новую строку
new_line proc
	mov ah, 2
	mov dl, 13
	int 21h
	mov dl, 10
	int 21h

	ret
new_line endp


read_string proc
	or cl, cl                          ; если равен 0 (а конец строки равен 0)
	jz read_string_exit                ; если конец найден строки

	push ax
	push bx
	push dx
	push si

	mov max_string_length, cl
	mov ah, 10
	mov dx, offset max_string_length     ; занести конец строки в dx
	int 21h

	xor bh, bh
	mov bl, min_string_length
	mov byte ptr[bx + char_massive], 0
	mov si, offset char_massive

	call copy_string

	pop si
	pop dx
	pop bx
	pop ax

read_string_exit:
  ret
read_string endp


; переместить в памяти блок байтов влево
move_memory_left proc
	jcxz move_memory_left_exit             ; если cx (количество перемещаемых байтов) равно 0 -> выход

	push cx                                ; сохранить изменяемые регистры
	push si                                ;
	push di                                ;

	add si, bx                             ; индекс строки источника S1
	add di, dx                             ; индекс строки назначения S2
	cld                                    ; автоувеличение si и di
	rep movsb                              ; (REPeat) si копировать в di, пока cx не равно нулю

	pop di                                 ; восстановить регистры
	pop si
	pop cx

move_memory_left_exit:
  ret
move_memory_left endp


; подсчет количества ненулевых символов в строке, адрес строки - DI
string_length proc
	push ax            ; сохраняем изменяемые регистры
	push di

	xor al, al
	mov cx, 0ffffh
	cld                ; автоувеличение di
	repnz scasb        ; (REPeat while Not Equal or Zero) искать al, пока адрес строки не равно null и cx не равно нулю
	not cx             ; логическое отрицание сх
	dec cx             ; вычитание 1 дает длину строки

	pop di             ; восстановить регистры
	pop ax

	ret
string_length endp


; скопировать одну строку в другую
copy_string proc
  push bx                  ; сохранить изменяемые регистры
	push cx                  ;
	push dx                  ;

	xchg si, di              ; переставить si и di
	call string_length       ; найти длину копируемой строки
	inc cx                   ; добить единицу для нулевого окончания
	xchg si, di              ; восстановить si и di
	xor bx, bx               ; индекс строки-источника = 0
	xor dx, dx               ; индекс строки, в которую производится копирование = 0
	call move_memory_left    ; копировать источник в назначение

	pop dx                   ; восстановить регистры
	pop cx
	pop bx

	ret
copy_string endp


; удаление лишних пробелов
delete_spaces proc
	push di
	push si
	push cx
	push dx

	mov si, offset string
	call string_length

  Cycle:
    mov dl, [di]             ; считать символ

    cmp dl, ' '              ; сравнить с пробелом
    jne rewrite_char         ; если не пробел - вывести

    cmp dx, '  '             ; а если пробел - то предыдущий был пробел или нет?
    je  next_char            ; если два пробела подряд - не печатаем

  rewrite_char:
    mov [si], dl
	  inc si

  next_char:
    mov dh, dl               ; сохранить текущий символ для теста на следующем витке
    inc di                   ; перейти кследующему символу

  loop Cycle

	mov byte ptr [si], ' '
	inc si
	mov byte ptr [si], 0

	pop dx
	pop cx
	pop si
	pop di

  ret
delete_spaces endp


task proc
push di
push cx

call string_length

cmp_cycle_1:
  cmp byte ptr [di], ''
  je task_end

  cmp byte ptr [di], 'a'
  je cmp_cycle_2
  cmp byte ptr [di], 'e'
  je cmp_cycle_2
  cmp byte ptr [di], 'i'
  je cmp_cycle_2
  cmp byte ptr [di], 'o'
  je cmp_cycle_2
  cmp byte ptr [di], 'u'
  je cmp_cycle_2
  cmp byte ptr [di], 'y'
  je cmp_cycle_2
  cmp byte ptr [di], 'A'
  je cmp_cycle_2
  cmp byte ptr [di], 'E'
  je cmp_cycle_2
  cmp byte ptr [di], 'I'
  je cmp_cycle_2
  cmp byte ptr [di], 'O'
  je cmp_cycle_2
  cmp byte ptr [di], 'U'
  je cmp_cycle_2
  cmp byte ptr [di], 'Y'
  je cmp_cycle_2

  jne go_next_symbol

  cmp_cycle_2:
    cmp byte ptr [di+1], ''
    je task_end

    cmp byte ptr [di+1], ' '
  	je go_next_symbol

    cmp byte ptr [di+1], 'a'
    je vowel_pair_found
    cmp byte ptr [di+1], 'e'
    je vowel_pair_found
    cmp byte ptr [di+1], 'i'
    je vowel_pair_found
    cmp byte ptr [di+1], 'o'
    je vowel_pair_found
    cmp byte ptr [di+1], 'u'
    je vowel_pair_found
    cmp byte ptr [di+1], 'y'
    je vowel_pair_found
    cmp byte ptr [di+1], 'A'
    je vowel_pair_found
    cmp byte ptr [di+1], 'E'
    je vowel_pair_found
    cmp byte ptr [di+1], 'I'
    je vowel_pair_found
    cmp byte ptr [di+1], 'O'
    je vowel_pair_found
    cmp byte ptr [di+1], 'U'
    je vowel_pair_found
    cmp byte ptr [di+1], 'Y'
    je vowel_pair_found
    jmp go_next_symbol

    vowel_pair_found:
      cmp byte ptr [di-1], ''
      je finding_new_word

      cmp byte ptr [di-1], ' '
      je finding_new_word

      jne go_back

        go_back:
          dec di
          jmp vowel_pair_found


        finding_new_word:
          cmp byte ptr [di], ''
          je task_end

          cmp byte ptr [di], ' '
          je go_next_symbol_after_print

          jne go_forward

          go_forward:
            call string_length

            mov cx, [di]
            mov ah, 02h
            mov dx, cx

            int 21h

            inc di
            jmp finding_new_word

  	go_next_symbol:
    	inc di
      jmp cmp_cycle_1

    go_next_symbol_after_print:
      call new_line

      inc di
      jmp cmp_cycle_1

task_end:
pop cx
pop di

ret
task endp


main:
	mov ax, @data
  mov ds, ax                    ; 16-разрядные регистры Data Degment'a
  mov es, ax                    ; Extra Segment'a

  mov ah, 09
  mov dx, offset input_message
  int 21h
  xor dx, dx

  mov di, offset string
  mov cl, 254

  call read_string               ; вызов процедуры чтения с клавиатуры

	call new_line                  ; перевод на новую строку в консоли
  call new_line

	call delete_spaces             ; удаление лишних пробелов из введенной строки

	call task                      ; поиск слов, в которых 2 повторяющихся гласных подряд

  call new_line

  mov ah, 4Ch
  int 21h

end main
