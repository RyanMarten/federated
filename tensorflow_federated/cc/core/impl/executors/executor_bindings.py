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
"""Python interface to C++ Executor implementations."""

from typing import Mapping

from tensorflow_federated.cc.core.impl.executors import _executor_bindings
from tensorflow_federated.python.core.impl.bindings_utils import data_conversions
from tensorflow_federated.python.core.impl.types import placements

# Import classes.
OwnedValueId = _executor_bindings.OwnedValueId
Executor = _executor_bindings.Executor

# Import executor constructors.
create_tensorflow_executor = _executor_bindings.create_tensorflow_executor
create_reference_resolving_executor = _executor_bindings.create_reference_resolving_executor
create_composing_executor = _executor_bindings.create_composing_executor

# Import executor constructor helpers.
create_insecure_grpc_channel = _executor_bindings.create_insecure_grpc_channel
GRPCChannel = _executor_bindings.GRPCChannelInterface


# Wrap any construction requiring cardinalities arguments to convert placement
# literals to strings.
def create_federating_executor(
    inner_executor: _executor_bindings.Executor,
    cardinalities: Mapping[placements.PlacementLiteral, int]
) -> _executor_bindings.Executor:
  """Constructs a FederatingExecutor with a specified placement."""
  uri_cardinalities = data_conversions.convert_cardinalities_dict_to_string_keyed(
      cardinalities)
  return _executor_bindings.create_federating_executor(inner_executor,
                                                       uri_cardinalities)


def create_remote_executor(
    channel: GRPCChannel,
    cardinalities: Mapping[placements.PlacementLiteral, int],
) -> _executor_bindings.Executor:
  """Constructs a RemoteExecutor proxying service on `channel`."""
  uri_cardinalities = data_conversions.convert_cardinalities_dict_to_string_keyed(
      cardinalities)
  return _executor_bindings.create_remote_executor(channel, uri_cardinalities)


def create_composing_child(
    executor: _executor_bindings.Executor,
    cardinalities: Mapping[placements.PlacementLiteral, int]
) -> _executor_bindings.Executor:
  """Constructs a ComposingChild with specified cardinalities."""
  uri_cardinalities = data_conversions.convert_cardinalities_dict_to_string_keyed(
      cardinalities)
  return _executor_bindings.create_composing_child(executor, uri_cardinalities)
