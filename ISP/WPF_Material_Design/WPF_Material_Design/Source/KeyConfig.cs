using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;

namespace WPF_Material_Design.Source
{
    class KeyConfig : ConfigurationSection
    {
        [ConfigurationProperty("SaveFile", IsRequired = true)]
        public KeyConfigElement Save => (KeyConfigElement)base["save"]; 
    }

    public class KeyConfigElement : ConfigurationElement
    {
        [ConfigurationProperty("key", IsRequired = true)]
        public string Key
        {
            get => (string)base["key"];
            set => base["key"] = value;
        }
    }
}
