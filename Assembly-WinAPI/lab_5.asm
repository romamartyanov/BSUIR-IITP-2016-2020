model	small
stack	256

.data

space db ' ', '$'
error_message db 'Cannot read file',10,13,'$'
input_warning db 10,13,'$'
out_of_range db 13, 10, 'STOP ' , 10, '$'                     ; db 13, 10 код инструкций для перехода на новую строку

input_file_name db 'matrix.txt',0
output_file_name db 'awnser.txt',0

array dw 1, 2, 3, 11, 42, -32, 5, -3, 0

buffer db 255 dup ('$')
buffer_2 db 255 dup ('$')
buffer_3 db 10 dup ('$')

plus_flag db 0
minus_flag db 0

max_array_length db 0

ten_const dw 10 ;0002
n dw 3

templen db ?
a db ?
handler dw ?


.code
.386

read_from_file proc		; ПОСЛЕ ПРОБЕЛА СРАБАТЫВАЕТ МЕТКА STORE

	push ax
	push bx
	push cx
	push dx

	mov ah, 3Dh									; открыть существующий файл
	mov al, 2										;
	lea dx, input_file_name			; с таким именем внутри сборки
	int 21h											;


	jnc not_n										; нет переполнения?
	lea dx, error_message				;
	mov ah, 09h									; вывести сообщение об ошибке
	int 21h											;
	jmp exit_main

	not_n:											; нет переполнения
		mov bx, ax								; прочитать
		mov ah, 3Fh								; инструкция для чтения из файла
		mov cx, 255								;
		lea dx, buffer						; куда считывать
		int 21h										;

	pop dx
	pop cx
	pop bx
	pop ax

	ret
read_from_file endp


fix_string proc

	push ax
	push bx
	push cx
	push dx
	push si
	push di

	cld

	lea si, buffer
	xor dl, dl

	bigc:
		lodsb

		cmp al, '$'
		je fexit

		cmp al, '.'
		je replace
		cmp al, 13
		je replace
		cmp al, 0Ah
		je replace
		cmp al, ','
		je replace
		cmp al, ':'
		je replace
		cmp al, ';'
		je replace
		cmp al, '('
		je replace
		cmp al, ')'
		je replace
		cmp al, '/'
		je replace
		cmp al, '\'
		je replace
		cmp al, '['
		je replace
		cmp al, ']'
		je replace
		cmp al, '*'
		je replace

		jmp bigc

	replace:
		mov di, si
		dec di
		mov al, ' '
		stosb

		jmp bigc

	fexit:

	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
fix_string endp

fix_spaces_in_string proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di


	lea si, buffer							; помещаем buffer в si
	xor dl, dl
	lea di, buffer_2

	big_cycle:
		lodsb											; mov al, [si]    inc si ; загрузка элемента из последовательности слов (цепочки) в регистр-аккумулятор al/ax/eax.
		cmp al, ' '
		je prob

		cmp al, '$'
		je quit

		stosb											; сохранение элемента из регистра-аккумулятора al/ax/eax в последовательности слов (цепочке)
		xor dl, dl
		jmp to_big_cycle

	prob:
		cmp dl, 1
		je big_cycle

		mov al, ' '
		stosb											; al -> es:[di]
		mov dl, 1

	to_big_cycle:
		jmp big_cycle

	quit:

	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
fix_spaces_in_string endp


convert_to_array proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

	mov a, 0

	cld
	xor cx, cx
	lea si, buffer_2

	xor di, di
	xor dl, dl

bf:
	xor ax, ax
	xor bx, bx
	mov a, 0

cont:
		lodsb
		cmp al, '$'
		je last_store

		cmp al, 45
		je minus    											; если нажат -, то запоминаем

		cmp al, ' '
		je stop

		cmp al, '0'
		jnl range													; если меньше нуля, то переходим к метке error

		jmp exception

	range:
		cmp al, '9'
		jng ff3	  												; если больше 9, то переходим к метке error
		jmp exception

	ff3:
		sub al, 48

		inc a															;
		xor ah, ah												; чистим верхний регистр
		xchg ax, bx												; в АХ кладем ранее введенную часть числа, а bx то, что ввели сейчас

		mul ten_const											; умножаем ранее введенную часть на 10
		jo exception											; если переполнение при умножении, то ошибка

		add bx, ax												; складываем с тем, что ввели сейчас
		jo exception											; если переполнение при умножении, то ошибка

	jmp cont														; продолжаем ввод

	minus:
		inc a
		mov minus_flag, 1

		neg bx

		jmp cont


	stop:
		cmp plus_flag, 1
		je store

		cmp minus_flag, 1
		jne notnegvalue

		; neg bx

	notnegvalue:
		mov n, bx
		mov plus_flag, 1

		jmp bf

	store:
		inc cx 																	; подсчет слов
		cmp minus_flag, 1
		jne notneg

	makeneg:
		neg bx

	notneg:
		mov array[di], bx
		inc di
		inc di
		mov minus_flag, 0

		push ax
		xor ax, ax
		mov al, a
		cmp max_array_length, al
		jg nextf
		mov max_array_length, al

	nextf:
		pop ax
		jmp bf

	last_store:
		inc cx

		cmp minus_flag, 1
		jne notneg2

		makeneg2:
			neg bx

		notneg2:
			mov array[di], bx
			inc di
			inc di

		push ax

		xor ax, ax
		mov al, a

		cmp max_array_length, al
		jg nextf_2

		mov max_array_length, al

		nextf_2:

	pop ax

	jmp finish


	exception:
		lea dx, error_message
		mov ah, 09h
		int 21h
		jmp exit_main

	finish:
		cmp n, 1
		je case_1

		cmp n, 2
		je case_2

		cmp n, 3
		je case_3

	case_1:
		cmp cx, 1
		je full_finish
		jmp exception

	case_2:
		cmp cx, 4
		je full_finish

		jmp exception

	case_3:
		mov ax, cx
		cmp cx, 9
		je full_finish

		jmp exception

	full_finish:
		mov a, 0

	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
convert_to_array endp


length_of_ax proc

	push ax
	push bx
	push cx
	push dx
	push si
	push di

	xor cx, cx
	test ax, 1000000000000000b
	js nega

	jmp r

	nega:
		neg ax
		inc cl

	r:
		xor dx, dx
		inc cx
		div ten_const
		cmp al, 0
		je m
		jmp r

	m:
		mov templen, cl

	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
length_of_ax endp


show_array proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

	mov	si, 0
	mov	cx, n

	external:																			; внешний цикл по строкам
		push cx																			; сохранение в стеке счётчика внешнего цикла
	  mov cx, n																		; для внутреннего цикла (по столбцам)

		internal:																		; внутренний цикл по строкам
		            																; сравниваем содержимое текущего элемента с искомым элементом:
			mov ax, array[si]													; templen - текущая длина  ;max_array_length - макс длина
			call length_of_ax

			mov bl, max_array_length
			sub bl, templen

			call signed_output

	space_begin:
		cmp bl, 0
		je space_end
		dec bl
		lea dx, space
		mov ah, 09h
		int 21h
		jmp space_begin


	space_end:
		lea dx, space
		mov ah, 09h
		int 21h

	  inc	si																				; передвижение на следующий элемент (2 bytes)
	  inc	si

		loop internal

	lea dx, input_warning
	mov ah, 09h
	int 21h

	pop	cx	            														; восстанавливаем cx из стека
	loop external																		; цикл (внешний)


	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
show_array endp


signed_output proc

	push ax
	push bx
	push cx
	push dx

	mov bx, ax
	mov ax, bx

	mov cx, 0 																				; счетчик символов

	test ax, 1000000000000000b
	js negative
	jmp cycle

negative:
	neg ax
	mov dx, 45   																			; символ -

	mov bx, ax
	mov ah, 02h
	int 21h

	mov ax, bx

cycle:
	xor dx, dx    																			; очищаем dx перед делением
	div ten_const																				; делим на 10
	push dx																							; остаток в стек
	inc cx		 																					; увеличиваем счетчик
	cmp ax, 0	 																					; если не ноль, то продолжаем делить
	jne cycle

popshow:		 																					; выводим из стека посимвольно
	pop dx
	add dx, 48

	mov ah, 02h
	int 21h

	loop popshow

	pop dx
	pop cx
	pop bx
	pop ax

	ret
signed_output endp


convert_to_string proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

	cmp ax,0
	je zero_case

	cmp minus_flag, 1
	jne no_minus
	neg ax

	no_minus:
		xor cx, cx
		xor dx, dx
		lea di, buffer_3

	zero_check:
		cmp ax, 0
		je konec
		xor dx, dx
		div ten_const
		push dx
		inc cx
		jmp zero_check

	konec:
		cmp minus_flag, 1
		jne skipff
		mov al, 45
		stosb

	skipff:
		pop ax
		add ax, 48
		stosb
		loop skipff
		jmp force_stop

	zero_case:
		lea di, buffer_3
		add ax, 48
		stosb

	force_stop:
	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
convert_to_string endp


save_to_file proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

	mov ah, 3Ch
	mov cx, 0
	lea	dx, output_file_name
	int 21h

	mov handler, ax
	xor ax, ax
	xor bx, bx
	lea si, buffer_3

	define_length:
		lodsb
		cmp al, '$'
		jz find_dollar
		inc bx
		jmp define_length

	find_dollar:
		mov cx, bx
		mov bx, handler
		mov ah, 40h
		lea dx, buffer_3
		int 21H

		mov ah, 3Eh		;ЗАКРЫТЬ ФАЙЛ
		int 21h


	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
save_to_file endp


singned_imul_check proc
	push ax

	add ax, 0
	jno next_operation_

	lea dx, out_of_range				;
	mov ah, 09h									; вывести сообщение об ошибке
	int 21h											;
	jmp exit_main

next_operation_:
	pop ax
	ret
singned_imul_check endp


first_order_determinant proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

		mov ax, array[0]								; det = a11

		add ax, 0

			jo out_of_range_ex_1

		call signed_output							; вывод ответа на экран

		mov minus_flag, 0
		test ax, 1000000000000000b
		jns to_convert_3

		mov minus_flag, 1

		to_convert_3:
			call convert_to_string
			call save_to_file

			lea dx, input_warning
			mov ah, 09h
			int 21h

			lea dx, input_warning
			mov ah, 09h
			int 21h
			jmp exit_1

out_of_range_ex_1:
	lea dx, out_of_range				;
	mov ah, 09h									; вывести сообщение об ошибке
	int 21h											;
	jmp exit_main

exit_1:
	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
first_order_determinant endp


second_order_determinant proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

		; номер элемента в массиве = (база + количество_элементов_в_строке * размер_элемента * i + j * размер_элемента)
		mov ax, array[4]								;
		mov bx, array[2]								; a21 * a12
		imul bx

			jo out_of_range_ex_2

		mov cx, ax

		mov ax, array[0]								;
		mov bx, array[6]								; a11 * a22
		imul bx													;

			jo out_of_range_ex_2

		sub ax, cx											; det = (a11 * a22) - (a21 * a12)

			jo out_of_range_ex_2

		call signed_output

		mov minus_flag, 0								;
		test ax, 1000000000000000b			; проверка на отрицательный ответ
		jns to_convert_2								; знак равен + (0)?

		mov minus_flag, 1								; тогда знак равен знак - (1)

		to_convert_2:
			call convert_to_string
			call save_to_file

			lea dx, input_warning
			mov ah, 09h
			int 21h

			lea dx, input_warning
			mov ah, 09h
			int 21h
			jmp exit_2

out_of_range_ex_2:
	lea dx, out_of_range				;
	mov ah, 09h									; вывести сообщение об ошибке
	int 21h											;
	jmp exit_main

exit_2:
	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
second_order_determinant endp


third_order_determinant proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

		; номер элемента в массиве = (база + количество_элементов_в_строке * размер_элемента * i + j * размер_элемента)
		mov ax, array[0]				;
		mov bx, array[8]				;
		imul bx									; a11 * a22 * a33
			jo out_of_range_ex_3

		mov bx, array[16]				;
		imul bx									;
			jo out_of_range_ex_3

		mov cx,ax								; a11 * a22 * a33

		mov ax, array[2]				;
		mov bx, array[10]				;
		imul bx									; a12 * a23 * a31
			jo out_of_range_ex_3

		mov bx, array[12]				;
		imul bx									;
			jo out_of_range_ex_3

		mov dx, ax
		mov ax, cx
		add ax, dx							; (a11 * a22 * a33) + (a12 * a23 * a31)
			jo out_of_range_ex_3

		mov cx, ax

		mov ax, array[4]				;
		mov bx, array[6]				;
		imul bx									; a13 * a21 * a32
			jo out_of_range_ex_3

		mov bx, array[14]				;
		imul bx									;
			jo out_of_range_ex_3

		mov dx, ax
		mov ax, cx
		add ax, dx							; (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32)
			jo out_of_range_ex_3

		mov cx, ax

		mov ax, array[0]				;
		mov bx, array[10]				;
		imul bx									; a11 * a23 * a32
			jo out_of_range_ex_3

		mov bx, array[14]				;
		imul bx									;
			jo out_of_range_ex_3

		mov dx, ax
		mov ax, cx
		sub ax, dx							; (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a11 * a23 * a32)
			jo out_of_range_ex_3

		mov cx, ax

		mov ax, array[2]				;
		mov bx, array[6]				;
		imul bx									; a12 * a21 * a33
			jo out_of_range_ex_3

		mov bx, array[16]				;
		imul bx									;
			jo out_of_range_ex_3

		mov dx, ax
		mov ax, cx
		sub ax, dx							; (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a11 * a23 * a32) - (a12 * a21 * a33)
			jo out_of_range_ex_3

		mov cx, ax

		mov ax, array[4]				;
		mov bx, array[8]				;
		imul bx									; a13 * a22 * a31
			jo out_of_range_ex_3
		mov bx, array[12]				;
		imul bx									;
			jo out_of_range_ex_3

		mov dx, ax
		mov ax, cx
		sub ax, dx							; det = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a11 * a23 * a32) - (a12 * a21 * a33) - (a13 * a22 * a31)
			jo out_of_range_ex_3

		call signed_output

		mov minus_flag, 0								;
		test ax, 1000000000000000b			; проверка на отрицательный ответ
		jns to_convert								  ; знак равен + (0)?

		mov minus_flag, 1								; тогда знак равен знак - (1)

		to_convert:
			call convert_to_string
			call save_to_file

			lea dx, input_warning
			mov ah, 09h
			int 21h
			jmp exit_3


out_of_range_ex_3:
	lea dx, out_of_range				;
	mov ah, 09h									; вывести сообщение об ошибке
	int 21h											;
	jmp exit_main


exit_3:
	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
third_order_determinant endp


determinant_counting proc
	push ax
	push bx
	push cx
	push dx
	push si
	push di

	mov	si, 0
	mov	cx, n

	cmp cx, 1											;
	jnl ff1												; cx не меньше 1
	jmp exit_determinant					; меньше 1

	ff1:
		cmp cx, 3										;
		jng ff2											; cx не больше 3
		jmp exit_determinant				; больше 3

	ff2:
		cmp cx, 1
		je first_order

		cmp cx, 2
		je second_order

		cmp cx, 3
		je third_order

	first_order:
		call first_order_determinant
		jmp exit_determinant

	second_order:
		call second_order_determinant
		jmp exit_determinant

	third_order:
		call third_order_determinant
		jmp exit_determinant

	exit_determinant:
	pop di
	pop si
	pop dx
	pop cx
	pop bx
	pop ax

	ret
determinant_counting endp


main:
	mov	ax, @data
	mov	ds, ax
	mov es, ax

	call read_from_file

	call fix_string
	call fix_spaces_in_string

	call convert_to_array
	call show_array

	call determinant_counting

	exit_main:
		mov	ax, 4c00h
		int	21h

end	main
