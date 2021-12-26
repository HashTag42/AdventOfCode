using System;   // Required to use the IEquatable interface.

/// This enum represents the possible sizes a cave can be.
enum CaveSize { BIG, small }

/// This class represents a cave.
/// It supports the IEquatable interface.
/// https://docs.microsoft.com/en-us/dotnet/api/system.iequatable-1
class Cave: IEquatable<Cave>
{
    /// This property represents the cave name.
    public string Name { get; init; }

    /// This property represents the cave size.
    public CaveSize Size { get; init; }

    /// Default constructor
    protected Cave()
    {

    }

    /// This constructor initializes the object.
    /// The cave size is derived from the casing in the Name string property.
    /// Big caves are written in uppercase; small caves are written in lowercase.
    public Cave(string Name)
    {
        this.Name= Name;
        this.Size= (this.Name == this.Name.ToUpper()) ? CaveSize.BIG : CaveSize.small;
    }

    /// This method compares two instances of this object.
    /// Two caves are equals when they have the same value on their Name property.
    public bool Equals(Cave Other)
    {
        bool isEqual= false;

        if(Other != null && this.Name == Other.Name)
        {
            isEqual= true;
        }

        return isEqual;
    }

    /// This methods supports the == operator.
    /// It is recommended when implementing the IEquatable interface.
    /// It must be a public static method.
    public static bool operator == (Cave A, Cave B)
    {
        bool result = false;

        if(null == (object)A || null == (object)B)
        {
            result = object.Equals(A, B);
        }
        else
        {
            result = A.Equals(B);
        }

        return result;
    }

    /// This methods supports the != operator.
    /// It is required when implementing the == operator.
    /// It must be a public static method.
    public static bool operator != (Cave A, Cave B)
    {
        bool result = false;

        if(null == (object)A || null == (object)B)
        {
            result = !object.Equals(A, B);
        }
        else
        {
            result = !A.Equals(B);
        }

        return result;
    }

    /// This is a required method to support the implementation of the IEquatable interface.
    public override bool Equals(object Object)
    {
        bool isEqual= false;

        if(Object != null && Object is Cave)
        {
            isEqual= Equals(Object);
        }

        return isEqual;
    }

    /// This is a required override method to support the implementation of the IEquatable interface.
    public override int GetHashCode() => this.Name.GetHashCode();

    /// This method provides a string representation for the object
    public override string ToString() => (this.Name + " (" + this.Size + ")");

}
