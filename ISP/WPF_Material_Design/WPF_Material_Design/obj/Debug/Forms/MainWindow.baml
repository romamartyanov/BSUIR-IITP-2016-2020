   M S B A M L   `   `   `  ����N  JWPF_Material_Design, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null9!clr-namespace:WPF_Material_DesignWPF_Material_Design  5   	   U QMaterialDesignThemes.Wpf, Version=2.3.1.953, Culture=neutral, PublicKeyToken=null{Sclr-namespace:MaterialDesignThemes.Wpf.Converters;assembly=MaterialDesignThemes.Wpf#MaterialDesignThemes.Wpf.Converters 5
   	   $    WPF_Material_Design.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   3local!clr-namespace:WPF_Material_Design     5   	   FmaterialDesign1http://materialdesigninxaml.net/winfx/xaml/themes  5	   	   rmaterialDesignConvertersSclr-namespace:MaterialDesignThemes.Wpf.Converters;assembly=MaterialDesignThemes.Wpf  5
   	     � Title$  Stellers Library��5   	   $	��720��6"   $
��1280��6/      MaterialDesignBody#���   5   	   $��Regular"�5   	   $��13(�5   	   &   System.Windows.Media.TextOptions   TextFormattingMode$ Ideal=�5   	      TextRenderingMode$
 Auto=�5   	     MaterialDesignPaper#���  5   	     MaterialDesignFont#���  5   	    � Icon$� �E:\University\Laboratory works\CSharp\wpf-labs-3rd-semestr\WPF_Material_Design\WPF_Material_Design\Data\Pictures\exlog_MIj_icon.ico��5   	    � 	Resources 5       �� MergedDictionaries �� Source  brushWatermarkBackground �� Color  brushWatermarkForeground  brushWatermarkBorder   BooleanToVisibilityConverter�� 5   
    5      �� 5      $h bpack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesignTheme.PopupBox.xaml?�6%   %�   &	       &	      &	 G     &	 g     �� 5      $ White��6?   �� 5      $ LightSteelBlue��6?   �� 5      $ Indigo��6;   �� 5       6+   5"      .��5'      � -   5         �Name$
 Menu��5'      .  (MaterialDesignThemes.Wpf.ColorZoneAssist	   Mode$	 
PrimaryMid=�5(      ���#f3f3f3
 � ColumnDefinitions
 5+   
   �� 5,      6!   �� 5-      6!   �� 5.      6!   �� 5/      6!   �� 50      6!   �� 51      6!   .+�55   
   �� $��1��6   $��5��56      ���#5029a9$��0,0,-0.4,0.4q�59      5<      �� 5>   
   ���#f3f3f3$��0,49,-0.4,0.4q�5?      $��6��5A      5B      �� 5D   
   $��0��6   ���#fefefe$��	0,0,0,0.4q�5F      +  %MaterialDesignThemes.Wpf.ShadowAssist   ShadowDepth$ Depth5=�5H      5J      �� 5N   
     SpecialButtonStyle#��[ 6   $��10,0,57,182.4q�6=   $��50��6T   $��Bottom=�6`   �� 5P   
   -   5        $��	exlog_pic��5Q      $��75,0,5,261.4q�5P        ExpressLogistic#��[ 5R      $��38��5S      $��Bottom=�6   �� 5U   
   -   5        $��exlog��5U       	 GeneralButtonStyle#��[	 6   $��20,0,142,273.4q�6J   $��Bottom=�6b   $��50��6}   $��50��6�   5W      �� 5Z   
   
�������$��55��6$   $��	0,0,0,0.4q�60   $��Bottom=�6C   $��Right=�6^   $��52��6z   .+�5[      A� $��50��6   $��50��6!    �� Bottom$ 0��6-   ��5\      
� 5]       
� RadiusX$ 1Q�6*    
� RadiusY$ 1Q�66    
� GradientOrigin$ 0.8, 0.2&�6B   .��5^      �  � Color$ White��6'    � Offset$
 0.01Q�65   � 5_      $ Indigo��6'   $ 1Q�66   5`       � Triggers 5c      :� 5d       :� RoutedEvent$ Window.Loaded��6#   .[�5e      �� .��5f      �� .��5g   "   U�  �� TargetProperty$ (Canvas.Bottom)�5h   !    g� Duration$ 0:0:3D�5i   !    g� AutoReverse .  g� RepeatBehavior$ Forever��5j   !    g� DecelerationRatio$ 1Q�6:   .\�5k   &   ��  O� KeyTime$ 0%��6;    O� Value$ 0Q�6H   �� 5l   &   $	 33%��6;   $ 60Q�6I   �� 5m   &   $	 66%��6;   $	 120Q�6I   �� 5n   &   $	 99%��6;   $	 180Q�6I   5o   #   �� 5q   "   $! Fill.GradientStops[1].Color�5r   !   $ 0:0:3D�5s   !   $ Forever��62    . g�5v   *   ��  �� KeyTime$ 0:0:1��6>    �� Value$ White��6N   �� 5w   *   $ 0:0:1��6>   $	 Red��6N   �� 5x   *   $ 0:0:1��6>   $ White��6N   5z   #   5{      5|      5}      5      5�      �� 5�   
   
�������$��	0,0,0,0.4q�6$   $
��Left=�67   $	��155��6R   $	��146��6^   $��Bottom=�6k   .+�5�      F� 
����  � 
 geometryPath#��[
 6!   
 �� Top$ 10��6F    �� Left$ 10��6V   A� 5�      $��15��6   $��15��6!   $ 10��6-   $ 10��6=   ��5�      
� 5�      $ 1Q�6*   $ 1Q�66   $ 0.7, 0.3&�6B   .��5�      � $ White��6'   $ 0Q�65   � 5�      $ 
BlueViolet��6'   $ 1Q�6:   5�       5�      :� 5�      $ Window.Loaded��6#   .[�5�      �� .��5�      �� .��5�   "   T� $ (Canvas.Top)�6;   $ 0:0:5D�5�   (   $ Forever��69    T� PathGeometry# [
 5�   (     T� Source$  Y=�6U   5�   #   T� 5�   "   $ (Canvas.Left)�6;   $ 0:0:5D�5�   (   $ Forever��69   # [
 5�   (   $  X=�6U   5�   #   5�      5�      5�      5�      5�      o� 5�   
   ! o� 
IsMainMenu! . ���#f3f3f3$��49��5�      $
��Left=�5�      $	��Top=�5�      .@�5�      m� -   5        $��MainMenu��5�      $�� ��5�        PrimaryHueDarkBrush#���  5�      $��49��5�      $��55��5�      " m� Icon" 5�      '  !MaterialDesignThemes.Wpf.PackIcon  5�      �  �ControlzEx.PackIconBase`1[[MaterialDesignThemes.Wpf.PackIconKind, MaterialDesignThemes.Wpf, Version=2.3.1.953, Culture=neutral, PublicKeyToken=null]]#   Kind$# DotsVertical=�6.   $��29��5�   .   $��
0,-6,-7,-7q�5�   .   $��23��5�   .   .@�5�      m� $0��*_Восстановление данных��6   " 5�        5�      $# BackupRestore=�62   $��29��5�   2   $��
0,-6,-7,-7q�5�   2   $��23��5�   2   .@�5�      m� -   5        $ m�Name$$ RecoveryCreate��5�      $3��-_Создать резервную копию��5�   #   " 5�      �� 5�       	 Shiba#��[ 6$   5�      m� 5�      -   5        $$ RecoveryLoad��5�      $7��1_Загрузить резервную копию��5�   #   " 5�      �� 5�      #��[ 6$   5�      5�      �� 5�      $��10��6   $��	0,0,0.4,0q�6(   m� 5�      -   5        $$ 	PluginsON��5�      $&�� _Включить плагины��5�      " 5�        5�      $
# Plus=�62   $��29��5�   .   $��
0,-6,-7,-7q�5�   .   $��23��5�   .   5�      m� 5�      -   5        $$ 
PluginsOFF��5�      $(��"_Отключить плагины��5�      " 5�        5�      $
# Plus=�62   $��29��5�   .   $��
0,-6,-7,-7q�5�   .   $��23��5�   .   % J� RenderTransformOrigin$% 0.5,0.5&�69   z�5�      V� 5�   "   .~�5�   &   �� �� 5�   &   �� 5�   &   & �� Angle$& 45Q�66   T� 5�   &   5�   #   5�      5�      �� 5�      $��10��6   $��	0,0,0.4,0q�6(   m� 5�      -	   5        $$ 	AboutMenu��5�      $��_About��6.   " 5�        5�      $# GithubCircle=�62   $��29��5�   .   $��
0,-6,-7,-7q�5�   .   $��23��5�   .   5�      5�      5      �� 5  
   -
   5        $��planets��5     $��Планеты��5     $
��Left=�5     $��0��5       MaterialDesignFlatButton#���  5     $% -3.104,1.829&�5
     $ 10��5     $	 145��5     $��10,192,10,0q�5     $��45��5     $	��Top=�5     5     �� 5  
   -   5        $��constallations��5     $��Созвездия��5     $
��Left=�5     $��0��5     #���  5     $ 10��5     $ 10��5     $% 0.5,0.5&�5     $��
10,57,10,0q�5     $��45��5      $	��Top=�5"     5$     �� 5&  
   -   5        $��stars��5&     $��Звезды��5(     $
��Left=�5)     $��0��5+     #���  5,     $ 10��5.     $	 100��5/     $��10,102,10,0q�50     $% 
0.468,-0.1&�51     $��45��52     $	��Top=�54     56     �� 58  
   -   5        $��
ngcObjects��58     $+��%Космические объекты��59     $
��Left=�5:     $��0��5<     #���  5=     $ 10��5?     $ 55��5@     $% 0.529,-0.049&�5A     $��10,147,10,0q�5B     $��45��5C     $	��Top=�5E     5G     �� 5I  
   -   5        ' ��Name$' NGCstackPanel��5I     $��10,256,10,0q�6,   $	��111��6A   $	��Top=�6N   $y�Hidden=�5J     .+�5K     �� $%��Показать только: ��6   $��20��5L     $��16(�5M     6(   �� 5O     -   5        $��Nebula��5O     $��Туманности��5P     �� 5Q     -   5        $��Open_cluster��5Q     $3��-Рассеянные зв. скопления��5R     �� 5S     -   5        $��Planetary_nebulae��5S     $1��+Планетарные туманности��5T     �� 5U     -   5        $��Globular_cluster��5U     $'��!Шаровые скопления��5V     �� 5W     -   5        $��Galaxy��5W     $��Галактики��5X     5[     �� 5]  
   -   5        ( ��Name$( Show_NGC_CheckBox��5]     $��Показать��5^     $y�Hidden=�5`     $��10,372,10,0q�5b     $��45��5c     #���  5d     $
��Left=�5e     $	��Top=�6S   �� 5i  
   -   5        $' StarsStackPanel��5i     $��10,256,10,0q�6.   $	��147��6C   $	��Top=�6P   $y�Hidden=�5j     .+�5k     �� $%��Показать только: ��6   $��20��5l     $��16(�5m     6(   �� 5o     -   5        $��Class_O��5o     $��Класс O��5p     �� 5q     -   5        $��Class_B��5q     $��Класс B��5r     �� 5s     -   5        $��Class_A��5s     $��Класс A��5t     �� 5u     -   5        $��Class_F��5u     $��Класс F��5v     �� 5w     -   5        $��Class_G��5w     $��Класс G��5x     �� 5y     -   5        $��Class_K��5y     $��Класс K��5z     �� 5{     -   5        $��Class_M��5{     $��Класс M��5|     5}     �� 5  
   -   5        $( Show_Stars_CheckBox��5     $��Показать��5�     $y�Hidden=�5�     $��10,408,10,0q�5�     $��45��5�     #���  5�     $
��Left=�5�     $	��Top=�6U   �� 5�  
   -   5        ) ��Name$) 
treeCanvas��5�     $��1��5�     $��2��5�     ���#fefefe$��9,57,5.8,0.4q�5�     $ Depth5=�5�     5�     �� 5�  
   $��16(�6   $��18,72,210.8,0q�6"   $
��Wrap=�69   $5��/Введите запрос                    ��6M   $	��Top=�5�     #��[ 5�     $��25��5�  �   $��2��6�   $��1��6�   y�6   �� * �� ElementName$* Search��+ �� Path$+ Text.IsEmpty�, �� 	Converter#, [ 6�   �� 5�  
   -   5        $��Search��5�     
������ #��[ 5�     $��18,65,18.8,0q�5�     $��32��6(   $	��Top=�5�     $��2��6*   $��1��6>   5�     R� 5�  
   -    5        $��MainTreeView��5�     $ 10��5�     $ 10��5�     $��2��5�     $��1��5�     $��18,102,18.6,80.4q�5�     5�     �� 5�  
   -!   5        $( 	move_left��5�     $��1��5�     - � ToolTip$- Предыдущие��5�     $��50��5�     $��50��5�      & "MaterialDesignFloatingActionButton#��[ 5�     $��18,0,0,10.4q�5�     $��Bottom=�5�     $
��Left=�6,   .��5�       $# MenuLeft=�6&   $��38��5�  &   $��38��5�  &   5�     �� 5�  
   -"   5        $( 
move_right��5�     $��1��5�     $- Следующие��5�     #���  5�     $��73,0,0,10.4q�5�     $��50��5�     $��50��5�     $��Bottom=�5�     $
��Left=�6,   .��5�       $# 	MenuRight=�6&   $��38��5�  &   $��38��5�  &   5�     �� 5�  
   -#   5        $
��Page��5�     $��1��5�     $��18(�5�     $
��Thin"�5�     $	 170��5�     $	 570��6"   $��83��63   $��128,0,0,10.4q�6>   $��1��6T   $
��Left=�6d   $��28��6   $��Bottom=�6�   '  !MaterialDesignThemes.Wpf.PopupBox  5�  
    - )MaterialDesignMultiFloatingActionPopupBox#��[ 5�  &   .   PlacementMode$. TopAndAlignCentres=�5�  &   /   UnfurlOrientation$/ Vertical=�5�  &   $/- )Управление элементами��5�  &   $��0,0,9.6,10.4q�5�  &   $��Right=�5�  &   $��Bottom=�6B   $��2��6]   $��50��6m   $��50��6y   $% 1.338,-1.608&�6�   0   PopupContent.0 5�     �� 1 �� Orientation$1 Vertical=�6   .+�5�     �� -$   5        $%- Добавить элемент��5�     $��45��5�     $��45��6%   .��5�       $
# Plus=�6.   $��20��5�  .   $��20��5�  .   5�     �� 5�     -%   5        $6- 0Удалить выбранный элемент��5�     $��45��5�     $��45��6%     PrimaryHueMidBrush#���  5�        PrimaryHueMidForegroundBrush#���  5�     .��5�       $# Delete=�6.   5�     5�     5�     �� 5�  
   $��3��6   $��3��5�     ���#fefefe$��9.2,57,9.6,0.4q�5�     $ Depth5=�5      5     �� 5  
   $ 10��5     $ 10��5     $- Designed by IrishLina��5     $��3��5	       	Shiba_PNG#��[ 5
     $��
0,65,9.6,0q�5     $	��190��5     $	��187��5     $	��Top=�5     $��Right=�5     �� 5  
   -&   5        $��Key_1��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $ 10��6L   $	��206��6\   $��20��6h   $��4��6t   $��
0,65,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -'   5        $��Key_2��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $ 30��6L   $	��206��6\   $��20��6h   $��4��6t   $��
0,85,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -(   5        2 ��Name$2 Key_3��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $ 50��6L   $	��206��6\   $��20��6h   $��4��6t   $��0,105,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -)   5        $2 Key_4��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $ 70��6L   $��20��6\   $	��206��6h   $��4��6t   $��0,125,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -*   5        $2 Key_5��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $ 90��6L   $	��206��6\   $��20��6h   $��4��6t   $��0,145,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -+   5        $2 Key_6��5     $
��Bold"�5     $	 207��6&   $
��Wrap=�68   $	 110��6L   $	��206��6]   $��20��6i   $��4��6u   $��0,165,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5  
   -,   5        $��Key_7��5     $
��Bold"�5      $	 207��6&   $
��Wrap=�68   $	 130��6L   $	��206��6]   $��20��6i   $��4��6u   $��0,185,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5!  
   --   5        $2 Key_8��5!     $
��Bold"�5"     $	 207��6&   $
��Wrap=�68   $	 150��6L   $	��206��6]   $��20��6i   $��4��6u   $��0,205,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5#  
   -.   5        $2 Key_9��5#     $
��Bold"�5$     $	 207��6&   $
��Wrap=�68   $	 170��6L   $	��206��6]   $��20��6i   $% 4.406,-9.01&�6u   $��4��6�   $��0,225,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 6�   $� ��6�   �� 6  �� 6  �� 6  �� 6  6&  �� 5%  
   -/   5        $��Key_10��5%     $
��Bold"�5&     $	 207��6&   $
��Wrap=�68   $	 190��6L   $	��206��6]   $��20��6i   $��4��6u   $��0,245,3.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5)  
   -0   5        $��Answer_1��5)     $	 418��5*     $
��Wrap=�6&   $ 10��6:   $	��190��6J   $��20��6V   $��5��6b   $��0,65,16.6,0q�6r   $��Right=�6�   $	��Top=�6�   �� 5+  
   -1   5        $��Answer_2��5+     $	 418��5,     $
��Wrap=�6&   $ 30��6:   $	��190��6J   $��20��6V   $��5��6b   $��0,85,16.6,0q�6r   $��Right=�6�   $	��Top=�6�   �� 5-  
   -2   5        $��Answer_3��5-     $	 418��5.     $
��Wrap=�6&   $ 50��6:   $��20��6J   $% 
0.936,1.48&�6V   $	��190��6y   $��5��6�   $��0,105,16.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 5/  
   -3   5        $��Answer_4��5/     $	 418��50     $
��Wrap=�6&   $ 70��6:   $	��190��6J   $��20��6V   $��5��6b   $��0,125,16.6,0q�6r   $��Right=�6�   $	��Top=�6�   �� 51  
   -4   5        $2 Answer_5��51     $	 418��52     $
��Wrap=�6&   $ 90��6:   $��20��6J   $	��190��6V   $��5��6b   $��0,145,16.6,0q�6r   $��Right=�6�   $	��Top=�6�   �� 53  
   -5   5        $��Answer_6��53     $	 418��54     $
��Wrap=�6&   $	 110��6:   $��20��6K   $% 
0.562,0.14&�6W   $	��190��6z   $��5��6�   $��0,165,16.6,0q�6�   $��Right=�6�   $	��Top=�6�   �� 55  
   -6   5        $��Answer_7��55     $	 418��56     $
��Wrap=�6&   $	 130��6:   $��20��6K   $	��190��6W   $��5��6c   $��0,185,16.6,0q�6s   $��Right=�6�   $	��Top=�6�   �� 57  
   -7   5        $2 Answer_8��57     $	 418��58     $
��Wrap=�6&   $	 150��6:   $	��190��6K   $��20��6W   $��5��6c   $��0,205,16.6,0q�6s   $��Right=�6�   $	��Top=�6�   �� 59  
   -8   5        $��Answer_9��59     $	 418��5:     $
��Wrap=�6&   $	 170��6:   $	��190��6K   $��20��6W   $��5��6c   $��0,225,16.6,0q�6s   $��Right=�6�   $	��Top=�6�   �� 5;  
   -9   5        $��	Answer_10��5;     $	 418��5<     $
��Wrap=�6&   $	 190��6:   $	��185��6K   $��20��6W   $��5��6c   $��0,245,21.6,0q�6s   $��Right=�6�   $	��Top=�6�   �� 5?  
   -:   5        $��	InfoBlock��5?     $ 10��5@     $	 215��5A     $
��Wrap=�5C     $	��328��5D     $��3��5F     $��3��5G     $��15.4,282,23.6,0q�5H     $	��Top=�5I     3 �� TextAlignment$3 Justify=�5K       5N  
   #��[ 5O  &   $. TopAndAlignCentres=�5P  &   $/ Vertical=�5Q  &   $/- )Управление элементами��5R  &   $��0,0,16.6,10.4q�5S  &   $��Right=�5T  &   $��Bottom=�6B   $��5��6]   $��50��6m   $��50��6y   $% 1.338,-1.608&�6�   .0 5V     �� $1 Vertical=�6   .+�5X     �� -;   5        $8- 2Изменить выбранный элемент��5X     $��45��5Y     $��45��6%   .��5[       $# Pencil=�6.   5\     �� 5^     -<   5        $6- 0Удалить выбранный элемент��5^     $��45��5`     $��45��6%   #���  5b     #���  5c     .��5d       $# Delete=�6.   5e     5g     5i     �� 5l  
   -=   5        $��	Flashback��5m     $����E:\University\Laboratory works\CSharp\wpf-labs-3rd-semestr\WPF_Material_Design\WPF_Material_Design\Data\Pictures\a_flashback_saigon_150427-3.jpg��5l     4 J� Opacity$	4 0.6Q�6�   $��6��5n     $��0,-238,-0.4,-211.6q�5o     $y�Hidden=�5p     �� 5r  
   ->   5        $��PluginButton��5r     #���  5s     $y�Hidden=�5u     $!��Убрать флешбек��5v     $
��Left=�5w     $ 10��5y     $	 638��5z     $��10,0,10,10.4q�5|     $��45��5}     $��Bottom=�68   5�     5�     