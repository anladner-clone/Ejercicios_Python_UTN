using System.Drawing;
using Veterinaria;

List <Cliente> listaClientes = new List <Cliente> ();
List <Animal> listaMascotas = new List <Animal> ();

while (true) {
   Console.WriteLine ("Opciones:");
   Console.WriteLine (" 1) Nuevo cliente");
   Console.WriteLine (" 2) Nueva mascota");
   Console.WriteLine (" 3) Mostrar mascotas");
   Console.WriteLine (" 4) Salir");
   Console.WriteLine ("");

   ConsoleKeyInfo tecla = Console.ReadKey (true);

   Console.WriteLine (tecla.KeyChar);

   if (tecla.Key == ConsoleKey.D1) { // Número 1: Nuevo cliente
      string nombre;
      string apellido;

      Console.Write ("Ingrese el nombre: ");
      nombre = Console.ReadLine ();
      Console.Write ("Ingrese el apellido: ");
      apellido = Console.ReadLine ();

      Cliente nuevoCliente = new Cliente (nombre, apellido);

      listaClientes.Add (nuevoCliente);
      Console.Write ("Nro. de cliente: " + listaClientes.IndexOf (nuevoCliente));
      Console.WriteLine ("\n");
   }
   else if (tecla.Key == ConsoleKey.D2) { // Número 2: Nueva mascota
      string nombre;
      int nroCliente;
      double peso;

      Console.Write ("Ingrese el nombre: ");
      nombre = Console.ReadLine ();
      Console.Write ("Ingrese el nro. de cliente del dueño: ");
      nroCliente = int.Parse (Console.ReadLine ());
      Console.Write ("Ingrese el peso: ");
      peso = double.Parse (Console.ReadLine ());

      while (true) {
         Console.WriteLine ("¿Qué animal es?:");
         Console.WriteLine (" a) Perro");
         Console.WriteLine (" b) Pez");
         Console.WriteLine (" c) ...");

         tecla = Console.ReadKey (true);

         Console.WriteLine (tecla.KeyChar);

         if (tecla.Key == ConsoleKey.A) { // Letra a: Perro
            string raza;

            Console.Write ("Ingrese la raza: ");
            raza = Console.ReadLine ();

            Perro nuevoPerro = new Perro (nombre, listaClientes.ElementAt (nroCliente), peso, raza);

            listaMascotas.Add (nuevoPerro);
            break;
         }
         else if (tecla.Key == ConsoleKey.B) { // Letra b: Pez
            string color;

            Console.Write ("Ingrese el color: ");
            color = Console.ReadLine ();

            Pez nuevoPez = new Pez (nombre, listaClientes.ElementAt (nroCliente), peso, color);

            listaMascotas.Add (nuevoPez);
            break;
         }
         //else if (...) { }
      }
      Console.WriteLine ("");
   }
   else if (tecla.Key == ConsoleKey.D3) { // Número 3: Mostrar mascotas
      Console.WriteLine ("Lista de mascotas registradas: ");

      foreach (Animal mascota in listaMascotas)
         Console.WriteLine (mascota.ResumenDatos ());

      Console.WriteLine ("");
   }
   else if (tecla.Key == ConsoleKey.D4) break; // Número 4: Salir
}