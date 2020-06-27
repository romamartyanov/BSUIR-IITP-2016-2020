using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WPF_Material_Design.Source
{
    [Serializable]
    public class Stars
    {
        public string Name { get; set; }
        public string ID { get; set; }
        public string Constellatoin { get; set; }

        public string Declination { get; set; }
        public string Right_Ascension { get; set; }

        public decimal? Weight { get; set; }
        public decimal? Radius { get; set; }
        public decimal? Apparent_Star_Magnitude { get; set; }
        public decimal? Star_Luminosity { get; set; }

        public string Star_Type { get; set; }
        public string Info { get; set; }
             

        public Stars()
        {
            Name = null;
            Constellatoin = null;
            Right_Ascension = null;
            Declination = null;

            Weight = null;
            Radius = null;
            Apparent_Star_Magnitude = null;
            Star_Luminosity = null;

            Star_Type = null;
            ID = null;
        }

        public void Create(string name,
                                    string constellatoin,
                                    string declination,
                                    string right_Ascension,

                                    decimal? weight,
                                    decimal? radius,

                                    decimal? apparent_Star_Magnitude,
                                    decimal? star_Luminosity,
                                    string star_type,

                                    string info)
        {
            this.Name = name;

            //this.Pic_Url = Console.ReadLine();

            this.Constellatoin = constellatoin;
            this.Declination = declination;

            this.Right_Ascension = right_Ascension;
            this.Weight = weight;
            this.Radius = radius;
            this.Apparent_Star_Magnitude = apparent_Star_Magnitude;
            this.Star_Luminosity = star_Luminosity;
            this.Star_Type = star_type;
            this.Info = info;

            this.ID = "Stars_" + this.Name.Replace(" ", "_").Replace("-", "_");
        }
    }
}
