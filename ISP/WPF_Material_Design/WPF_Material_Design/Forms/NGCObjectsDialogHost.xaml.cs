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
    /// Interaction logic for NGCObjectsDialogHost.xaml
    /// </summary>
    public partial class NGCObjectsDialogHost : Window
    {
        List<NGCObjects> NGCObjects = new List<WPF_Material_Design.Source.NGCObjects>();
        bool new_NGCObject = true;
        NGCObjects NGCObject;


        public NGCObjectsDialogHost(ref List<NGCObjects> NGCObjects)
        {
            InitializeComponent();

            this.NGCObjects = NGCObjects;
            new_NGCObject = true;
        }


        public NGCObjectsDialogHost(NGCObjects NGCObject)
        {
            InitializeComponent();

            Name.Text = NGCObject.Name;
            Constellatoin.Text = Convert.ToString(NGCObject.Constellatoin);

            Declination.Text = Convert.ToString(NGCObject.Declination);
            Right_Ascension.Text = Convert.ToString(NGCObject.Right_Ascension);
            Apparent_Star_Magnitude.Text = Convert.ToString(NGCObject.Apparent_Star_Magnitude);
            Redshift.Text = Convert.ToString(NGCObject.Redshift);
            Distance.Text = Convert.ToString(NGCObject.Distance);

            Type.Text = Convert.ToString(NGCObject.Type);

            Info.Text = Convert.ToString(NGCObject.Info);

            new_NGCObject = false;
            this.NGCObject = NGCObject;
        }


        private void accept_Click(object sender, RoutedEventArgs e)
        {
            NGCObjects NGCObject = new WPF_Material_Design.Source.NGCObjects();

            decimal? apparent_Star_Magnitude;
            decimal? redshift;

            ulong? distance;


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

                redshift = Convert.ToDecimal(Redshift.Text);

            }

            catch (Exception ex)
            {
                Redshift.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {

                distance = Convert.ToUInt64(Distance.Text);

            }

            catch (Exception ex)
            {
                Distance.Clear();

                MessageBox.Show("Введите заново");
                return;
            }


            if (new_NGCObject)
            {
                NGCObject.Create(Name.Text, Constellatoin.Text, Declination.Text, Right_Ascension.Text, apparent_Star_Magnitude, redshift, distance, Type.Text, Info.Text);
                NGCObjects.Add(NGCObject);
            }
            else
            {
                this.NGCObject.Create(Name.Text, Constellatoin.Text, Declination.Text, Right_Ascension.Text, apparent_Star_Magnitude, redshift, distance, Type.Text, Info.Text);
            }

            Close();
        }

        private void cancel_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
