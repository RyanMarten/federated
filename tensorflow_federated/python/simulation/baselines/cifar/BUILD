load("@rules_python//python:defs.bzl", "py_library", "py_test")

package_group(
    name = "default_visibility",
    includes = ["//tensorflow_federated/python/simulation:simulation_visibility"],
    packages = [
        # Subpackages
        "//tensorflow_federated/python/simulation/baselines/cifar/...",
    ],
)

package(default_visibility = [":default_visibility"])

licenses(["notice"])

py_library(
    name = "cifar",
    srcs = ["__init__.py"],
    srcs_version = "PY3",
    visibility = ["//tensorflow_federated/python/simulation/baselines:__pkg__"],
)

py_library(
    name = "cifar_preprocessing",
    srcs = ["cifar_preprocessing.py"],
    srcs_version = "PY3",
    deps = [
        "//tensorflow_federated/python/core/api:computation_base",
        "//tensorflow_federated/python/core/api:computations",
        "//tensorflow_federated/python/core/impl/types:computation_types",
    ],
)

py_test(
    name = "cifar_preprocessing_test",
    size = "medium",
    srcs = ["cifar_preprocessing_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":cifar_preprocessing",
        "//tensorflow_federated/python/core/backends/native:execution_contexts",
    ],
)

py_library(
    name = "cifar100_tasks",
    srcs = ["cifar100_tasks.py"],
    srcs_version = "PY3",
    deps = [
        ":cifar_preprocessing",
        ":resnet_models",
        "//tensorflow_federated/python/learning:keras_utils",
        "//tensorflow_federated/python/learning:model",
        "//tensorflow_federated/python/simulation/baselines:baseline_task",
        "//tensorflow_federated/python/simulation/baselines:client_spec",
        "//tensorflow_federated/python/simulation/baselines:task_data",
        "//tensorflow_federated/python/simulation/datasets:cifar100",
    ],
)

py_test(
    name = "cifar100_tasks_test",
    srcs = ["cifar100_tasks_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":cifar100_tasks",
        "//tensorflow_federated/python/core/backends/native:execution_contexts",
        "//tensorflow_federated/python/simulation/baselines:baseline_task",
        "//tensorflow_federated/python/simulation/baselines:client_spec",
    ],
)

py_library(
    name = "resnet_models",
    srcs = ["resnet_models.py"],
    srcs_version = "PY3",
    deps = ["//tensorflow_federated/python/simulation/models:group_norm"],
)

py_test(
    name = "resnet_models_test",
    srcs = ["resnet_models_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [":resnet_models"],
)
