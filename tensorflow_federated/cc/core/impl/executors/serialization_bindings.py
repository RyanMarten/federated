# Copyright 2021, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Python interface to C++ Value serialization implementations."""

from tensorflow_federated.cc.core.impl.executors import _serialization_bindings

# Protobuf constructors.
Value = _serialization_bindings.Value
Sequence = _serialization_bindings.Sequence
Struct = _serialization_bindings.Struct
Element = _serialization_bindings.Element
Federated = _serialization_bindings.Federated
Cardinality = _serialization_bindings.Cardinality

# Serialization methods.
serialize_tensor_value = _serialization_bindings.serialize_tensor_value
deserialize_tensor_value = _serialization_bindings.deserialize_tensor_value
