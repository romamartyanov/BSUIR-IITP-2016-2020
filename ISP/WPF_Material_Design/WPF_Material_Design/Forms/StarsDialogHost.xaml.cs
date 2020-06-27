using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using WPF_Material_Design.Source;



namespace WPF_Material_Design.Forms
{
    /// <summary>
    /// Interaction logic for StarsDialogHost.xaml
    /// </summary>
    /// 

    public partial class StarsDialogHost : Window
    {
        List<Stars> Stars = new List<WPF_Material_Design.Source.Stars>();

        bool new_star = true;
        Stars star;


        public StarsDialogHost(ref List<Stars> stars)
        {
            InitializeComponent();
            Stars = stars;

            new_star = true;
        }


        public StarsDialogHost(Stars star)
        {
            InitializeComponent();

            Name.Text = Convert.ToString(star.Name);

            Constellatoin.Text = Convert.ToString(star.Constellatoin);

            Declination.Text = Convert.ToString(star.Declination);
            Right_Ascension.Text = Convert.ToString(star.Right_Ascension);

            Weight.Text = Convert.ToString(star.Weight);
            Radius.Text = Convert.ToString(star.Radius);

            Apparent_Star_Magnitude.Text = Convert.ToString(star.Apparent_Star_Magnitude);
            Star_Luminosity.Text = Convert.ToString(star.Star_Luminosity);
            Star_Type.Text = Convert.ToString(star.Star_Type);

            Info.Text = Convert.ToString(star.Info);

            new_star = false;
            this.star = star;
        }


        private void accept_Click(object sender, RoutedEventArgs e)
        {
            Stars star = new WPF_Material_Design.Source.Stars();

            decimal? weight;
            decimal? radius;

            decimal? apparent_Star_Magnitude;
            decimal? star_Luminosity;


            try
            {
                weight = Convert.ToDecimal(Weight.Text);
                
            }

            catch (Exception ex)
            {
                Weight.Clear();
                
                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                radius = Convert.ToDecimal(Radius.Text);

            }

            catch (Exception ex)
            {
                Radius.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                apparent_Star_Magnitude = Convert.ToDecimal(Apparent_Star_Magnitude.Text);

            }

            catch (Exception ex)
            {
                Apparent_Star_Magnitude.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                star_Luminosity = Convert.ToDecimal(Star_Luminosity.Text);

            }

            catch (Exception ex)
            {
                Star_Luminosity.Clear();

                MessageBox.Show("Введите заново");
                return;
            }


            if (new_star)
            {
                star.Create(Name.Text, Constellatoin.Text, Declination.Text, Right_Ascension.Text, weight, radius, apparent_Star_Magnitude, star_Luminosity, Star_Type.Text, Info.Text);
                Stars.Add(star);
            }
            else
            {
                this.star.Create(Name.Text, Constellatoin.Text, Declination.Text, Right_Ascension.Text, weight, radius, apparent_Star_Magnitude, star_Luminosity, Star_Type.Text, Info.Text);
            }

            Close();
        }


        private void cancel_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
