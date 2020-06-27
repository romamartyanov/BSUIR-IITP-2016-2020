using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace WPF_Material_Design.Source
{
    [Serializable]
    public class MassiveCollection<T> : ICollection<T>, INotifyPropertyChanged
    {
        private T[] counters = new T[0];
        private int count = 0;


        public int Count
        {
            get
            {
                return count;
            }
        }

        public bool IsReadOnly
        {
            get
            {
                return false;
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyChanged([CallerMemberName]string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        }


        public void Add(T item)
        {
            if (count + 1 >= counters.Length)
            {
                Array.Resize(ref counters, counters.Length + 1);
            }

            counters[count++] = item;
        }

        public void Add(params T[] items)
        {
            for (int i = 0; i < items?.Length; i++)
            {
                Add(items[i]);
            }
        }

        public void Clear()
        {
            Array.Clear(counters, 0, counters.Length);
            Array.Resize(ref counters, 1);
        }

        public bool Contains(T item)
        {
            foreach (object x in counters)
            {
                if (x.Equals(item))
                    return true;
            }
            return false;
        }

        public void CopyTo(T[] array, int arrayIndex)
        {
            throw new NotImplementedException();
        }

        public IEnumerator<T> GetEnumerator()
        {
            return ((IEnumerable<T>)counters).GetEnumerator();
        }

        public bool Remove(T item)
        {
            bool flag = false;
            for (int i = 0; i < counters.Length; i++)
            {
                if (counters[i].Equals(item))
                {
                    for (int j = i; i < counters.Length - 1; i++)
                        counters[i] = counters[i + 1];
                    flag = true;
                    break;
                }
            }

            if (flag)
            {
                count--;
                if (counters.Length / 4 >= count)
                    Array.Resize(ref counters, count);
            }
            return flag;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return (this as IEnumerable<T>).GetEnumerator();
        }
    }
}
