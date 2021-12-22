using System.Diagnostics;

class Packet
{

    public Packet()
    {
        Debug.WriteLine("New Packet!");
    }

    class Header
    {
        private enum type {literalType, operatorType};

        class Version
        {

        }

        class TypeID
        {


        }
    }
}