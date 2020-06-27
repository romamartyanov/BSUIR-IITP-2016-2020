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

namespace WPF_Material_Design
{
    /// <summary>
    /// Interaction logic for win_1.xaml
    /// </summary>
    public partial class PlanetsDialogHost : Window

    {
        List<Planets> Planets = new List<WPF_Material_Design.Source.Planets>();
        bool new_planet = true;
        Planets planet;


        public PlanetsDialogHost(ref List<Planets> planets)
        {
            InitializeComponent();
            Planets = planets;

            new_planet = true;
        }


        public PlanetsDialogHost(Planets planet)
        {
            InitializeComponent();

            Name.Text = Convert.ToString(planet.Name);

            Radius.Text = Convert.ToString(planet.Radius);
            Weigth.Text = Convert.ToString(planet.Weight);

            Circulation_Period_Axis.Text = Convert.ToString(planet.Circulation_Period_Axis);
            Circulation_Period.Text = Convert.ToString(planet.Circulation_Period);
            Center_body.Text = Convert.ToString(planet.Center_body);
            Orbit_Radius.Text = Convert.ToString(planet.Orbit_Radius);
            Eccentricity.Text = Convert.ToString(planet.Eccentricity);
            Info.Text = Convert.ToString(planet.Info);

            new_planet = false;
            this.planet = planet; 
        }


        private void accept_Click(object sender, RoutedEventArgs e)
        {
            Planets planet = new WPF_Material_Design.Source.Planets();



            decimal? radius;
            decimal? weigth;
            decimal? circulation_Period_Axis;
            decimal? circulation_Period;
            decimal? orbit_Radius;
            decimal? eccentricity;

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
                weigth = Convert.ToDecimal(Weigth.Text);

            }
            catch (Exception ex)
            {
                Weigth.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                circulation_Period_Axis = Convert.ToDecimal(Circulation_Period_Axis.Text);

            }
            catch (Exception ex)
            {
                Circulation_Period_Axis.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                circulation_Period = Convert.ToDecimal(Circulation_Period.Text);

            }
            catch (Exception ex)
            {
                Circulation_Period.Clear();

                MessageBox.Show("Введите заново");
                return;
            }

            try
            {
                orbit_Radius = Convert.ToDecimal(Orbit_Radius.Text);

            }
            catch (Exception ex)
            {
                Orbit_Radius.Clear();

                MessageBox.Show("Введите заново");
                return;


            }

            try
            {
                eccentricity = Convert.ToDecimal(Eccentricity.Text);

            }
            catch (Exception ex)
            {
                Eccentricity.Clear();

                MessageBox.Show("Введите заново");
                return;


            }


            if (new_planet)
            {
                planet.Create(Name.Text, radius, weigth, circulation_Period_Axis, circulation_Period, Center_body.Text, orbit_Radius, eccentricity, Info.Text);
                Planets.Add(planet);
            }
            else
            {
                this.planet.Create(Name.Text, radius, weigth, circulation_Period_Axis, circulation_Period, Center_body.Text, orbit_Radius, eccentricity, Info.Text);
            }

            Close();
        }


        private void cancel_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
