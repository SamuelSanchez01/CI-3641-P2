# Particular llamarme Samuel Sánchez eh?

Bueno, toca Taylor Suif otra vez

# Lenguaje Swift

## Descripción

Swift es un lenguaje de programación de propósito general, multi-paradigma y compilado, creado por Apple en 2014. Está diseñado para ser seguro, rápido y expresivo, y se utiliza principalmente para el desarrollo de aplicaciones para productos Apple

## Estructuras de control de flujo

### Condicionales

"if" "else if" "else"

``` 
Let n = 132
if n % 3 == 0 {
    print("Divisible entre 3")
}else if n % 3 == 1 {
    print("Resto 1 al dividir entre 3")
}else{
    print("Resto 2 al dividir entre 3")
}
```

### Switch/Case/Default

```
let deporte = "fulvo"
switch {
    case "fulvo":
        print("muga fulvo")
    case "basketball":
        print("muga basket")
    default"
        print("juguemos otro deporte")
}
```

### Ciclos

While:

```
var i = 1
while i < 11 {
    print(i)
    i += 1
}
```

For

```
for i in 1...10 {
    print(i)
}
```

Repeat

```
var j = 1
repeat {
    print(j)
    j += 1
} while j < 11
```

## Evaluacion de Expresiones y Funciones

Swift utiliza principalmente la evaluación aplicativa

Swift evalua de izquierda a derecha