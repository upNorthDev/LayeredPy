# LayeredPy

**LayeredPy** is a Python library built to implement a clean, maintainable layered architecture. It offers support for service-oriented programming and includes built-in dependency injection (DI) to improve code modularity and testability.

---

## Features

- **Layered Architecture**: Enables a structured and modular separation of concerns.
- **Dependency Injection**: Dependencies get injected automatically, improving testability and reducing tight coupling.
- **Service Management**: Defines base services with extensible behavior for your application logic.
- **CLI Tool**: Generate service boilerplate with the `service` tool.

---

## Installation

Install **LayeredPy** using `pip`:

```bash
pip install layered-py
```

---

## Getting Started

Here’s how you can use **LayeredPy** in your projects.

---

### 1. Define and Register a Service
Create a service by subclassing the `Service` class and use the `@register` decorator to register it.

```python
from layered_py.service import Service
from layered_py.decorators import register_service


@register("GreetingService")
class GreetingService(Service):
    def say_hello(self):
        print("Hello from LayeredPy!")
```

---

### 2. Inject the Service Where Needed
With the `@inject` decorator, services can be directly injected as attributes of the class. You don’t need to pass them explicitly.

```python
from layered_py.decorators import inject


class MyApp:
    @inject("GreetingService")
    def run(self):
        self.GreetingService.say_hello()  # Directly access the injected service


# Example usage
if __name__ == "__main__":
    app = MyApp()
    app.run()
```

#### Output:
> Hello from LayeredPy!

---

### 3. Generate Service Templates with the CLI
You can use the built-in `layeredpy` CLI tool to create new service boilerplates automatically.

The CLI tool of LayeredPy can create services, repositories, domains and presentation classes

#### Example Usage:

```bash
layeredpy create MyNewService
```

This command generates the following `services/MyNewService.py` file:

```python
from layered_py.service import BaseService

@register('MyNewService')
class MyNewService(BaseService):
    def setup(self):
        pass

    def handle(self):
        raise NotImplementedError
```

## Create complete class sets with 'layeredpy generate'

LayeredPy is capable of creating complete sets of classes for example this command:

```bash
layeredpy generate User
```

will create a **UserService, UserRepository, User and UserRoutes** with the register annotation so they are DI-ready.

## License

This project is licensed under the [MIT License](LICENSE).

---

## Support

For questions or support, feel free to open an issue on the [GitHub Issues](https://github.com/upNorthDev/LayeredPy/issues) page. You can find more information on the [project repository](https://github.com/upNorthDev/LayeredPy).

