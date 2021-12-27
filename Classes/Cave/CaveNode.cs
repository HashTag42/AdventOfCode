using System;                       // Required to use the IEquatable interface.
using System.Collections.Generic;   // Required to use the List class.

/// This class represents a Cave that's connected to other caves.
class CaveNode : Cave, IEquatable<CaveNode>
{
    /// This property stores all caves linked to the object.
    public List<Cave> Links { get; private set; }

    public int Visited { get; set; }

    /// The default constructor initializes the object properties.
    public CaveNode()
    {
        Links   = new List<Cave>();
        Visited = 0;
    }

    /// This constructor creates an object from a cave.
    public CaveNode(string Name) : this()
    {
        base.Name = Name;
    }

    /// This method allows the user to link other caves to the object.
    /// Links are only added when don't yet exist.
    public void Add(Cave LinkedCave)
    {
        if(!Links.Contains(LinkedCave))
        {
            Links.Add(LinkedCave);
        }
    }

    /// This method supports the equality check between objects of the same type.
    public bool Equals(CaveNode Other)
    {
        bool result = false;
        if(!base.Equals(Other))
        {
            result = false;
        }
        else
        {
            if(Name == Other.Name)
            {
                result = true;
            }
        }

        return result;
    }

    /// This override method is required to implement the IEquatable interace.
    public override bool Equals(object obj)
    {
        bool result = false;

        if (obj == null || GetType() != obj.GetType())
        {
            result = false;
        }
        else
        {
            result = this.Equals (obj);
        }

        return result;
    }

    /// This override method is required to implement the IEquatable interface.
    public override int GetHashCode() => base.GetHashCode();

    /// This override method returns a string representation for the object.
    public override string ToString()
    {
        string outputString = null;
        string separator = ", ";

        outputString += this.Name + ": ";
        foreach(Cave linkedCave in Links)
        {
            outputString += linkedCave.Name + separator;
        }
        // Remove the trailing separator
        outputString = outputString.Substring(0, outputString.Length - separator.Length);

        return outputString;
    }

}