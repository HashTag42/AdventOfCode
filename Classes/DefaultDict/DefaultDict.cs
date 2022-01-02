#nullable disable

using System;
using System.Collections.Generic;

class DefaultDict<TKey, TValue>
{
    private Dictionary<TKey, List<TValue>> dic { get; set; }

    public DefaultDict() => this.dic = new Dictionary<TKey, List<TValue>>();

    public List<TValue> GetValues(TKey Key)
    {
        List<TValue> values;
        if(dic[Key] != null)
        {
            values = dic[Key];
        }
        else
        {
            values = new List<TValue>();
        }
        return values;
    }

    public void Add(TKey Key, TValue Value)
    {
        // Adding the Key only if it doesn't already exists in the Dictionary.
        if(!dic.ContainsKey(Key))
        {
            List<TValue> empty = new List<TValue>();
            dic.Add(Key, empty);
        }

        // Adding the Value only if it doesn't already exist in the list of values for the given Key.
        List<TValue> values = this.GetValues(Key);
        // if(!values.Contains(Value))
        // {
            values.Add(Value);
        // }
        dic[Key] = values;
    }

    public override string ToString()
    {
        string output = "";

        foreach(TKey key in this.dic.Keys)
        {
            output += $"{key}: ";
            foreach(TValue value in this.GetValues(key))
            {
                output += $"{value} ";
            }
            output += Environment.NewLine;
        }

        return output;
    }

}