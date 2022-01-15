
# BUCLE FOR

# Example 1
frutas = ['apple', 'banana', 'cherry', 'orange']

for fruta in frutas:
    print("la fruta es " + str(fruta))


# Example 2
apodos = ['Jesus David Gordito', 'Ranita', 'Viejita', 'bodoque', 'chiquita']

mensajeFinal = 'Hola que tal familia, mando saludos para:'

for apodo in apodos:
    mensajeFinal = mensajeFinal + ', ' + apodo


# 'Hola que tal familia, mando saludos para:'
# ciclo 0: 'Hola que tal familia, mando saludos para:, Jesus David Gordito'
# ciclo 1: 'Hola que tal familia, mando saludos para:, Jesus David Gordito, Ranita'
# ciclo 2: 'Hola que tal familia, mando saludos para:, Jesus David Gordito, Ranita, Viejita'
# ciclo 3: 'Hola que tal familia, mando saludos para:, Jesus David Gordito, Ranita, Viejita, bodoque'
# ciclo 4: 'Hola que tal familia, mando saludos para:, Jesus David Gordito, Ranita, Viejita, bodoque, chiquita'


print(mensajeFinal)
