using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WPF_Material_Design.Source
{
    [Serializable]
    public class Planets
    {
        public string Name { get; set; }
        public string ID { get; set; }

        //public override string Pic_Url { get; set; }

        public decimal? Radius { get; set; }
        public decimal? Weight { get; set; }


        public decimal? Circulation_Period_Axis { get; set; }
        public decimal? Circulation_Period { get; set; }
        public string Center_body { get; set; }

        public decimal? Orbit_Radius { get; set; }
        public decimal? Eccentricity { get; set; }

        public string Info { get; set; }



        public Planets()
        {
            Name = null;
            ID = null;
            //Pic_Url = null;

            Radius = null;
            Weight = null;
            
            Circulation_Period_Axis = null;
            Center_body = null;
            Circulation_Period = null;
            
            Orbit_Radius = null;
            Eccentricity = null;
            Info = null;
        }

        public void Create(string name,
                            decimal? radius,
                            decimal? weigth,

                            decimal? circulation_Period_Axis,
                            decimal? circulation_Period,
                            string center_body,
                            decimal? orbit_Radius,
                            decimal? eccentricity,
                            string info)
        {
            this.Name = name;

            //this.Pic_Url = Console.ReadLine();

            this.Radius = radius;
            this.Weight = weigth;
            
            this.Circulation_Period_Axis = circulation_Period_Axis;
            this.Circulation_Period = circulation_Period;
            this.Center_body = center_body;      
            this.Orbit_Radius = orbit_Radius;
            this.Eccentricity = eccentricity;
            this.Info = info;

            this.ID = "Planets_" + this.Name.Replace(" ", "_").Replace("-", "_");
        }               
    }
}
