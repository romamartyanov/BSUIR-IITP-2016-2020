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

#pragma warning disable CS0108

namespace WPF_Material_Design.Forms
{
    /// <summary>
    /// Interaction logic for ConstalltionsDialogHost.xaml
    /// </summary>
    public partial class ConstellationsDialogHost : Window
    {
        List<Constellations> Constellations = new List<WPF_Material_Design.Source.Constellations>();

        bool new_constellation = true;
        Constellations constellation;


        public ConstellationsDialogHost(ref List<Constellations> constellations)
        {
            InitializeComponent();
            Constellations = constellations;

            new_constellation = true;
        }


        public ConstellationsDialogHost(Constellations constellation)
        {
            InitializeComponent();

            Name.Text = Convert.ToString(constellation.Name);

            Right_Ascension_from.Text = Convert.ToString(constellation.Right_Ascension_from);
            Right_Ascension_to.Text = Convert.ToString(constellation.Right_Ascension_to);

            Declination_from.Text = Convert.ToString(constellation.Declination_from);
            Declination_to.Text = Convert.ToString(constellation.Declination_to);

            Info.Text = Convert.ToString(constellation.Info);

            new_constellation = false;
            this.constellation = constellation;
        }


        private void accept_Click(object sender, RoutedEventArgs e)
        {
            Constellations constellation = new WPF_Material_Design.Source.Constellations();
           

            Close();

            if (new_constellation)
            {
                constellation.Create(Name.Text, Declination_from.Text, Declination_to.Text, Right_Ascension_from.Text, Right_Ascension_to.Text, Info.Text);
                Constellations.Add(constellation);
            }
            else
            {
                this.constellation.Create(Name.Text, Declination_from.Text, Declination_to.Text, Right_Ascension_from.Text, Right_Ascension_to.Text, Info.Text);
            }

            Close();
        }


        private void cancel_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
