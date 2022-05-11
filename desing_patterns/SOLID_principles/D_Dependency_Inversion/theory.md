# Principio de Inversion de Dependencias (PID)
## Definicion
__*Los modulos de alto nivel no deben depender de los modulos de bajo nivel, sino que ambos deben depender de sus abstracciones.*__

__*Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abtracciones.*__

## Interpretacion

### Modulos de alto y bajo nivel
Cuando nos referimos a *__modulos de alto nivel__*, hacemos referencia a aquellas partes de nuestro codigo que llama o invoca a acciones de *otros*, y estos "otros" son a lo que llamamos *__modulos de bajo nivel__*, que suelen ser partes del codigo que cumplen tareas como conexion y consultas a bases de datos, operaciones complejas, etc. (es decir, pueden/suelen ser consideradas las librerias de las que depende nuestro codigo)

### Abstracciones y detalles
Normalmente cuando se comienza a desarrollar, en lo primero que se piensa son en lo que llamamos __concreciones__, que no son mas que las clases concretas que poseen atributos y metodos concretos (es decir, con implementacion de codigo), y posteriormente en base a lo que se penso para la __concrecion__ se define una interfaz o clase abstracta segun sea el caso. Sin embargo, lo que la segunda premisa nos indica, es que debemos hacer lo opuesto, primero pensar en definir buenas interfaces y luego implementar sus concreciones en base a estas.

## Metodos de implementacion de PID
La forma en la que se puede aplicar el Principio de Inversion de dependencias es mediante:
- Inyeccion de dependencias
- Inversion de Control (IoC)

### Inyeccion de dependencias

Basicamente, consiste en remover la responsabilidad de instanciar objetos de una clase, a la que llamaremos Cliente, a otro lugar. Posteriormente, el Cliente recibira de alguna forma las dependencias que necesita ya instanciadas, removiendo de esa forma el acoplamiento que existiria si el Cliente se encargara de instanciar sus propios objetos.

Algunas formas de recibir las dependencias son:
- #### Inyeccion por constructor
```
public class ClassA {
    private SomeDependency someDep;

    public ClassA (SomeDependency someDep) {
        this.someDep = someDep;
    }
}
```
Consiste en recibir la instancia de la dependencia mediante el constructor de la clase al momento de instanciarla.

- #### Inyeccion por parametros
```
public class ClassA {
    public void someMethod(SomeDependency someDep) {
        someDep.useService();
    }
}
```
La dependencia se recibe al momento de invocar el metodo que la utiliza.

- #### Inyeccion por setter
```
public class ClassA {
    private SomeDependency someDep = null;

    public setSomeDep(SomeDependency someDep) {
        this.someDep = someDep;
    }
}
```
La dependencia se recibe en algun momento de la vida del objeto mediante el setter del mismo. Esta forma tiene la ventaja de que es posible variar a lo largo de la ejecucion la instancia de la dependencia.

### Inversion de Control (IoC)
 La inversion de control se refiere a que la aplicacion delega de alguna forma el flujo de control en un tercero, generalmente un framework. El framework se encarga de gestion el ciclo de vida de la aplicacion e ira notificandola sobre eventos, para que esta actue en consecuencia.
