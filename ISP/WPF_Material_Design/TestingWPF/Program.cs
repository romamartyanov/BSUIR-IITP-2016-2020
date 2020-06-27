using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestingWPF
{
    class Program
    {
        static void Main(string[] args)
        {
        }
    }

    public class ConfigWork : ConfigurationSection
    {
        [ConfigurationProperty("save", IsRequired = false)]
        public Element Save
        {
            get
            {
                return (Element)base["save"];
            }
        }

        [ConfigurationProperty("new", IsRequired = false)]
        public Element New
        {
            get
            {
                return (Element)base["new"];
            }
        }

        [ConfigurationProperty("open", IsRequired = false)]
        public Element Open
        {
            get
            {
                return (Element)base["open"];
            }
        }


        [ConfigurationProperty("path", IsRequired = false)]
        public Element Path
        {
            get
            {
                return (Element)base["path"];
            }
        }

    }


    public class Element : ConfigurationElement
    {
        [ConfigurationProperty("key", IsRequired = false)]
        public string Key
        {
            get
            {
                return (string)base["key"];
            }
            set
            {
                base["key"] = value;
            }
        }

        [ConfigurationProperty("value", IsRequired = false)]
        public string Value
        {
            get
            {
                return (string)base["value"];
            }
            set
            {
                base["value"] = value;
            }
        }
    }
}
