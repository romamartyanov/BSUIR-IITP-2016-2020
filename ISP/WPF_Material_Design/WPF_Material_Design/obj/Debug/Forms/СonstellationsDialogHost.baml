   M S B A M L   `   `   `  ����N  JWPF_Material_Design, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullE'clr-namespace:WPF_Material_Design.FormsWPF_Material_Design.Forms  5   	   8    2WPF_Material_Design.Forms.ConstellationsDialogHost   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   9local'clr-namespace:WPF_Material_Design.Forms     5   	     � Title$  Созвездия��5   	    � Icon$� zE:\University\Laboratory works\CSharp\wpf-labs-3rd-semestr\WPF_Material_Design\WPF_Material_Design\Data\Pictures\Shiba.ico��5	   	   $��451.388��5
   	   $��448.2��6    � 
ResizeMode$ NoResize=�5   	    � 	Resources 5         brushWatermarkBackground �� Color  brushWatermarkForeground  brushWatermarkBorder   BooleanToVisibilityConverter  EntryFieldStyle �� 
TargetType �� Property �� Value��%!  &	        &	      &	 G     &	 g     &	 z     �� 5   
   $ White��6;   �� 5   
   $ LightSteelBlue��6;   �� 5   
   $ Indigo��67   �� 5   
   6'   �� 5   
   " �6(   .�5      ��  � ��$ Stretch=�64   �� 5       � ��$ Center=�62   5      5      .��5      � #��[  6   #��[ 5      $��	0,0,3.6,0q�5      $	��Top=�6   $	��411��66   .+�5    
   �� $
��Left=�6   $��	10,10,0,0q�5!      $
��Wrap=�5"      $	��Top=�5#      $��13(�5$      $	��165��6"   $��18��6.   �� 6;   $�Созвез��6?   �� 6O   $�дия��6S   �� 6`   �� 6l   6s   �� 5&   
   $��16(�6   $��10,33,11.6,0q�6"   $
��Wrap=�68   $��Имя:��6L   $	��Top=�6X   #��[ 5'      y�5(      ��  �� ElementName$
 Name��	 �� Path$	 Text.IsEmpty�
 �� 	Converter#
 [ �� 5)   
   -   5        $
��Name��5)      
������ #��[ 67   $��
10,33,10,0q�6k   $��27��6   $	��Top=�6�   �� 5+   
   $��16(�6   $��
10,68,11,0q�6"   $
��Wrap=�66   $��Склонение от:��6J   $	��Top=�6_   #��[ 5,      y�5-      �� $ Right_Ascension_from��$	 Text.IsEmpty�#
 [ �� 5.   
   -   5        $��Right_Ascension_from��5.      
������ #��[ 6G   $��
10,65,10,0q�6{   $��30��6�   $	��Top=�6�   �� 50   
   $��16(�6   $��10,103,11.6,0q�6"   $
��Wrap=�69   $��Склонение до:��6M   $	��Top=�6b   #��[ 51      y�52      �� $ Right_Ascension_to��$	 Text.IsEmpty�#
 [ �� 53   
   -   5        $��Right_Ascension_to��53      
������ #��[ 6E   $��10,100,10,0q�6y   $��29��6�   $	��Top=�6�   �� 55   
   $��16(�6   $��10,138,9.6,0q�6"   $
��Wrap=�68   $/��)Прямое восхождение от:��6L   $	��Top=�6j   #��[ 56      y�57      �� $ Declination_from��$	 Text.IsEmpty�#
 [ �� 58   
   -   5        $��Declination_from��58      
������ #��[ 6C   $��10,129,10,0q�6w   $��35��6�   $	��Top=�6�   �� 5:   
   $��16(�6   $��9,173,9.6,0q�6"   $
��Wrap=�67   $/��)Прямое восхождение до:��6K   $	��Top=�6i   #��[ 5;      y�5<      �� $ Declination_to��$	 Text.IsEmpty�#
 [ �� 5=   
   -   5        $��Declination_to��5=      
������ #��[ 6A   $��10,171,10,0q�6u   $��31��6�   $	��Top=�6�   �� 5A   
   $��16(�6   $��
10,338,6,0q�6"   $
��Wrap=�66   $��Информация:��6J   $	��Top=�6]   #��[ 5B      $��25��5C   �   y�6   �� $
 Info��$	 Text.IsEmpty�#
 [ 6�   �� 5D   
   -   5        $
��Info��5D      
������ #��[ 67   $��10,205,10,0q�6k   $	��158��6�   $	��Top=�6�   �� 5G   
   -   5         ��Name$ accept��5G      $��42��5H      $��Добавить��5I        MaterialDesignFlatButton#���  5J       �� Left$ 10��5K      
 �� Top$ 55��5L       J� RenderTransformOrigin$ 0.529,-0.049&�5M      $��
12,368,0,0q�5N      $
��Left=�6%   $	��206��6@   $	��Top=�6L   6d   �� 5P   
   -   5        $ cancel��5P      $��42��5Q      $��Отменить��5R      #���  5S      $��	0,368,7,0q�5T      $��Right=�6$   $	��206��6@   $ 0.5,0.5&�6L   $	��Top=�6l   6�   5W      5X      