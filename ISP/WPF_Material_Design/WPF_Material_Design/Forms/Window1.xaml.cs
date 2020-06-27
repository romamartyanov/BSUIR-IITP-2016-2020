using System;
using System.IO;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Media.Animation;

namespace WPF_Material_Design.Forms
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        int i = 1;

        public Window1()
        {
            InitializeComponent();

            //CreateDynamicWrapPanel();
            
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            ListBoxItem item = new ListBoxItem() { Content = i };

            DoubleAnimation buttonAnimation = new DoubleAnimation();
            buttonAnimation.From = listbox.ActualHeight;
            buttonAnimation.By = 20;
            buttonAnimation.Duration = TimeSpan.FromSeconds(1);
            listbox.BeginAnimation(ListBox.HeightProperty, buttonAnimation);

            listbox.Items.Add(item);
            i++;
        }

        private void listbox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }


        //private void CreateDynamicWrapPanel()
        //{
        //    string[] lines_columns = File.ReadAllText(@"E:\rect.txt").Split(' ');
        //    int columns = Convert.ToInt32(lines_columns[0]);
        //    int lines = Convert.ToInt32(lines_columns[1]);

        //    double actualWidth = window.Width;
        //    double actualHeight = window.Height;

        //    double rectWidth = window.Width / columns;
        //    double rectHeight = window.Height / lines;


        //    myWrapPanel.ItemHeight = rectHeight;
        //    myWrapPanel.ItemWidth = rectWidth;

        //    bool white = true;

        //    for (int i = 0; i < lines; i++)
        //    {
        //        for (int j = 0; j < columns; j++)
        //        {
        //            Rectangle rect = new Rectangle();
        //            if (white)
        //            {
        //                rect.Fill = Brushes.White;
        //                white = false;
        //            }

        //            else
        //            {
        //                rect.Fill = Brushes.Black;
        //                white = true;
        //            }

        //            rect.Height = rectHeight;
        //            rect.Width = rectWidth;

        //            myWrapPanel.Children.Add(rect);
        //        }

        //        if (columns % 2 == 0)
        //        {
        //            if (white)
        //                white = false;
        //            else
        //                white = true;
        //        }
        //    }

        //}
    }

    public class PercentageConverter : MarkupExtension, IValueConverter
    {
        private static PercentageConverter _instance;


        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            return System.Convert.ToDouble(value) + System.Convert.ToDouble(parameter);
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }


        public override object ProvideValue(IServiceProvider serviceProvider)
        {
            return _instance ?? (_instance = new PercentageConverter());
        }
    }

    public class Extention : MarkupExtension
    {
        public double Height { get; set; }
        public double Width { get; set; }
        public double Min { get; set; }

        public Extention() { }

        public override object ProvideValue(IServiceProvider sp)
        {
            if (Width < Height)
                Min = Width;
            else
                Min = Height;
            return Min;
        }
    }
}

