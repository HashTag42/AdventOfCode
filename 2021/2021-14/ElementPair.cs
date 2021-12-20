using System;

public class ElementPair : IEquatable<ElementPair>
{
    public char First { get; init; }
    public char Second { get; init; }

    public ElementPair(char[] Pair)
    {
        this.First  = Pair[0];
        this.Second = Pair[1];
    }

    public ElementPair(string Pair)
    {
        this.First  = Pair[0];
        this.Second = Pair[1];
    }

    public ElementPair(char First, char Second)
    {
        this.First  = First;
        this.Second = Second;
    }

    public bool Equals(ElementPair Other)
    {
        bool areEquals = false;
        if(null != Other)
        {
            if( this.First  == Other.First
            &&  this.Second == Other.Second)
            {
                areEquals = true;
            }
        }
        return areEquals;
    }

    public override bool Equals(object obj)
    {
        bool areEquals = false;
        if(null != obj)
        {
            ElementPair pair = obj as ElementPair;
            if(null != pair)
            {
                areEquals = Equals(pair);
            }
        }
        return areEquals;
    }

    public static bool operator == (ElementPair pair1, ElementPair pair2)
    {
        bool result = false;

        if(null == (object)pair1 || null == (object)pair2)
        {
            result = object.Equals(pair1, pair2);
        }
        else
        {
            result = pair1.Equals(pair2);
        }

        return result;
    }

    public static bool operator != (ElementPair pair1, ElementPair pair2)
    {
        bool result = false;

        if(null == (object)pair1 || null == (object)pair2)
        {
            result = ! object.Equals(pair1, pair2);
        }
        else
        {
            result = ! pair1.Equals(pair2);
        }

        return result;
    }

    public override int GetHashCode()
    {
        return (First + Second).GetHashCode();
    }

    public override string ToString()
    {
        return (First.ToString() + Second.ToString());
    }
}
