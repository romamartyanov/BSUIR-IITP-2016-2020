#include <windows.h>
#include <tchar.h>

#include "stdafx.h"
#include "WindowsProject.h"


#define MAX_LOADSTRING 100

int ID_MYBUTTON = 1;																// идентификатор для кнопочки внутри главного окна

LRESULT CALLBACK MainWinProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);	// Процедура обработки сообщений окна
																					// hwnd - дескриптор окна, которому предназначено сообщение
																					// код сообщения
																					// wp и lp - 32-битные параметры сообщения, интерпретация которых зависит от кода сообщения

int x = 0, y = 0;																	// координаты нажатий ЛКМ

int xArray[500];																	// Массивы точек рисунка
int yArray[500];																	//

int count = 0;																		// кол-во нажатий ЛКМ

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR LpCmdLine, int nCmdShow)
{
	WNDCLASSEX wc;																	// Структура WNDCLASSEX Содержит информацию о классе окон.Он используется с функциями RegisterClassEx и GetClassInfoEx.
	wc.cbSize = sizeof(wc);															// величина структуры в байтах
	wc.style = CS_HREDRAW | CS_VREDRAW;												// перерисовывать окно при движении по гор/верт
	wc.lpfnWndProc = MainWinProc;													// процедура обработки событий окна

	wc.cbClsExtra = 0;																// число дополнительных байтов в конце структуры
	wc.cbWndExtra = 0;																// число дополнительных байтов при создании экземпляра приложения

	wc.hInstance = hInstance;														// Обработчик экземпляра, который содержит процедуру окна для класса.
	wc.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_APPLICATION));				// дескриптор иконки окна
	wc.hCursor = LoadCursor(NULL, IDC_ARROW);										// дескриптор курсора мыши для окна
	wc.hbrBackground = (HBRUSH)(COLOR_WINDOW);										// дескриптор "кисточки" для закрашивания фона окна

	wc.lpszMenuName = NULL;															// имя ресурса, содержащего меню окна
	wc.lpszClassName = _T("Drawing");												// имя класса

	wc.hIconSm = LoadIcon(wc.hInstance, MAKEINTRESOURCE(IDI_APPLICATION));

	if (!RegisterClassEx(&wc))														// обработка ошибки если класс не зарагистрировался
	{
		MessageBox(NULL, _T("Class crearing error"), _T("Error"), MB_OK);
		return 0;
	}

	HWND hMainWnd = CreateWindow(				// HWND - дескриптор окна
		_T("Drawing"),							// загловок окна
		_T("Drawing"),
		WS_OVERLAPPEDWINDOW,					// Режим отображения
												// "перекрываемое" окно с системным меню, кнопками сворачивания/разворачивания, рамкой изменения размеров, короче, типичный стиль для главного окна приложения

		CW_USEDEFAULT,							// Положение окна по оси ОХ
		CW_USEDEFAULT,							// Позиция окна по оси у 

		CW_USEDEFAULT,							// Ширина окна
		CW_USEDEFAULT,							// Высота

		NULL,									// Дескриптор родительского
		NULL,									// Дескриптор меню
		hInstance,
		NULL									// Передача в WM_CREATE
	);

	if (!hMainWnd) {
		MessageBox(NULL, _T("Window crearing error"), _T("Error"), MB_OK);
		return NULL;							// Выходим из приложения
	}
	
	ShowWindow(hMainWnd, nCmdShow);
	UpdateWindow(hMainWnd);

	MSG msg;

	while (GetMessage(&msg, NULL, 0, 0)) {
		DispatchMessage(&msg);
	}
	return msg.wParam;
}


LRESULT CALLBACK MainWinProc(HWND hw, UINT msg, WPARAM wp, LPARAM lp) {			// процедура обработки сообщений для главного окна
																				// hwnd - дескриптор окна, которому предназначено сообщение
																				// код сообщения
																				// wp и lp - 32-битные параметры сообщения, интерпретация которых зависит от кода сообщения
	
	HDC hdc;																	// Обработчик контекста устройства (DC).		
	PAINTSTRUCT paintstruct;													// содержит информацию для приложения. Эта информация может использоваться для рисования клиентской области окна, принадлежащего этому приложению

	switch (msg) {
		case WM_CREATE:

			/* При создании окна добавляем кнопку */
			CreateWindow(
				_T("button"),								//
				_T("Clear"),								// текст кнопки
				WS_CHILD | BS_PUSHBUTTON | WS_VISIBLE,

				10,											//
				10,											// координаты кнопки
				150,										//
				30,											//

				hw,
				(HMENU)ID_MYBUTTON,
				NULL,
				NULL
			);
			return 0;

		case WM_COMMAND:														// сообщение от команды меню или управляющего элемента
			if ((HIWORD(wp) == 0) && (LOWORD(wp) == ID_MYBUTTON)) {				// нажата наша кнопка?
				InvalidateRect(NULL, NULL, true);								// Функция InvalidateRect добавляет прямоугольник в область обновления указанного окна. 
																				// Область обновления представляет собой часть клиентской области окна, которая должна быть перерисована
				count = 0;
			}
			return 0;

		case WM_LBUTTONDOWN: {

			x = LOWORD(lp);														// loword - извлекает старшее слово из данного 32-разрядного значения
			y = HIWORD(lp);														// hiword - извлекает старшее слово из данного 32-разрядного значения
		
			xArray[count] = x;
			yArray[count] = y;

			count++;

			InvalidateRect(hw, NULL, FALSE);
			return 0;
		}

		case WM_PAINT: {
			hdc = BeginPaint(hw, &paintstruct);									// возвращает дескриптор контекста устройства экрана для указанного окна

			HPEN pen = CreatePen(PS_SOLID, 2, RGB(0, 0, 0));					// создаем перо черного цвета
			HPEN oldPen = (HPEN)SelectObject(hdc, pen);
			HBRUSH  brush_white = CreateSolidBrush(RGB(220, 220, 220));			// добавляем различных стилей для рисования фигур
			HBRUSH  brush_red = CreateSolidBrush(RGB(255, 0, 0));				//
			HBRUSH  brush_black = CreateSolidBrush(RGB(0, 0, 0));				//

			for (int i = 0; i < count; i++) {
				// Ставим карандаш на место, куда нажали мышкой
				x = xArray[i];
				y = yArray[i];	
				MoveToEx(hdc, x, y, NULL);

				// Белым цветом рисуем два прямоугольника (первую ступень)
				SelectObject(hdc, brush_white);
				Rectangle(hdc, x, y, x + 60, y + 300);
				Rectangle(hdc, x, y + 140, x + 60, y + 300);


				// С помощью многоугольника (poly) рисуем переход от одной ступени к другой
				POINT poly_roof_1[4] = {
					{ x, y },
					{ x + 10 , y - 10 },
					{ x + 50, y - 10 },
					{ x + 60, y }
				};
				
				SelectObject(hdc, brush_red);
				Polygon(hdc, poly_roof_1, 4);

				// Рисуем вторую ступень
				SelectObject(hdc, brush_white);
				Rectangle(hdc, x + 10, y - 10, x + 50, y - 180);


				// Смещаем точку, откуда рисуем
				x = xArray[i] + 10;
				y = yArray[i] - 180;
				MoveToEx(hdc, x, y, NULL);


				// Переход от 2 ступени к 3
				POINT poly_roof_2[4] = {
					{ x, y },
					{ x + 10 , y - 10 },
					{ x + 10 + 20, y - 10 },
					{ x + 10 + 10 + 20, y }
				};

				SelectObject(hdc, brush_red);
				Polygon(hdc, poly_roof_2, 4);


				// Опять смещаем
				x = xArray[i] + 10 + 10;
				y = yArray[i] - 180  - 10;
				MoveToEx(hdc, x, y, NULL);
						

				// Рисуем последнюю ступень с помощью многоугольника
				POINT poly_roof_3[5] = {
					{ x, y },
					{ x , y - 100 },
					{ x + 20 / 2, y - 100 - 20 },
					{ x + 20, y - 100},
					{ x + 20, y }
				};

				SelectObject(hdc, brush_red);
				Polygon(hdc, poly_roof_3, 5);


				// Рисуем стабилизирующие двигатели на первой ступени			
				x = xArray[i] - 10;
				y = yArray[i] + 300 + 20;
				MoveToEx(hdc, x, y, NULL);

				POINT poly_engine_1[4] = {
					{ x, y },
					{ x , y - 50 },
					{ x + 10, y - 10 - 50},
					{ x + 10, y }
				};

				SelectObject(hdc, brush_black);
				Polygon(hdc, poly_engine_1, 4);


				x = xArray[i] + 25;
				y = yArray[i] + 300 + 20;
				MoveToEx(hdc, x, y, NULL);

				POINT poly_engine_2[5] = {
					{ x, y },
					{ x , y - 50 },
					{ x + 10 / 2, y - 10 - 50 },
					{ x + 10, y - 50},
					{ x + 10, y }
				};

				SelectObject(hdc, brush_black);
				Polygon(hdc, poly_engine_2, 5);


				x = xArray[i] + 60;
				y = yArray[i] + 300 + 20;
				MoveToEx(hdc, x, y, NULL);

				POINT poly_engine_3[4] = {
					{ x, y },
					{ x , y - 60 },
					{ x + 10, y - 50 },
					{ x + 10, y }
				};

				SelectObject(hdc, brush_black);
				Polygon(hdc, poly_engine_3, 4);

			}

			SelectObject(hdc, oldPen);
			DeleteObject(pen);
			DeleteObject(brush_white);
			DeleteObject(brush_red);
			DeleteObject(brush_black);

			EndPaint(hw, &paintstruct);

			return 0;
		}
	
		case WM_DESTROY:									// сообщение об уничтожении окна
			PostQuitMessage(0);
			return 0;
	}

	return DefWindowProc(hw, msg, wp, lp);					// вызывается функция, если процедура не обрабатывает какое-то сообщение (возвращает его системе для обработки по умолчанию
}


