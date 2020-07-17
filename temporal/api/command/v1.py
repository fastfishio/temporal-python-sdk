# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/command/v1/message.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from temporal.api.common import v1 as v1common
from temporal.api.enums import v1 as v1enums
from temporal.api.failure import v1 as v1failure
from temporal.api.taskqueue import v1 as v1taskqueue


@dataclass
class ScheduleActivityTaskCommandAttributes(betterproto.Message):
    activity_id: str = betterproto.string_field(1)
    activity_type: v1common.ActivityType = betterproto.message_field(2)
    namespace: str = betterproto.string_field(3)
    task_queue: v1taskqueue.TaskQueue = betterproto.message_field(4)
    header: v1common.Header = betterproto.message_field(5)
    input: v1common.Payloads = betterproto.message_field(6)
    # Indicates how long the caller is willing to wait for an activity
    # completion. Limits for how long retries are happening. Either this or
    # start_to_close_timeout_seconds must be specified. When not specified
    # defaults to the workflow execution timeout.
    schedule_to_close_timeout_seconds: int = betterproto.int32_field(7)
    # Limits time an activity task can stay in a task queue before a worker picks
    # it up. This timeout is always non retryable as all a retry would achieve is
    # to put it back into the same queue. Defaults to
    # schedule_to_close_timeout_seconds or workflow execution timeout if not
    # specified.
    schedule_to_start_timeout_seconds: int = betterproto.int32_field(8)
    # Maximum time an activity is allowed to execute after a pick up by a worker.
    # This timeout is always retryable. Either this or
    # schedule_to_close_timeout_seconds must be specified.
    start_to_close_timeout_seconds: int = betterproto.int32_field(9)
    # Maximum time between successful worker heartbeats.
    heartbeat_timeout_seconds: int = betterproto.int32_field(10)
    # Activities are provided by a default retry policy controlled through the
    # service dynamic configuration. Retries are happening up to
    # schedule_to_close_timeout. To disable retries set
    # retry_policy.maximum_attempts to 1.
    retry_policy: v1common.RetryPolicy = betterproto.message_field(11)


@dataclass
class RequestCancelActivityTaskCommandAttributes(betterproto.Message):
    scheduled_event_id: int = betterproto.int64_field(1)


@dataclass
class StartTimerCommandAttributes(betterproto.Message):
    timer_id: str = betterproto.string_field(1)
    start_to_fire_timeout_seconds: int = betterproto.int64_field(2)


@dataclass
class CompleteWorkflowExecutionCommandAttributes(betterproto.Message):
    result: v1common.Payloads = betterproto.message_field(1)


@dataclass
class FailWorkflowExecutionCommandAttributes(betterproto.Message):
    failure: v1failure.Failure = betterproto.message_field(1)


@dataclass
class CancelTimerCommandAttributes(betterproto.Message):
    timer_id: str = betterproto.string_field(1)


@dataclass
class CancelWorkflowExecutionCommandAttributes(betterproto.Message):
    details: v1common.Payloads = betterproto.message_field(1)


@dataclass
class RequestCancelExternalWorkflowExecutionCommandAttributes(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    workflow_id: str = betterproto.string_field(2)
    run_id: str = betterproto.string_field(3)
    control: str = betterproto.string_field(4)
    child_workflow_only: bool = betterproto.bool_field(5)


@dataclass
class SignalExternalWorkflowExecutionCommandAttributes(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    execution: v1common.WorkflowExecution = betterproto.message_field(2)
    signal_name: str = betterproto.string_field(3)
    input: v1common.Payloads = betterproto.message_field(4)
    control: str = betterproto.string_field(5)
    child_workflow_only: bool = betterproto.bool_field(6)


@dataclass
class UpsertWorkflowSearchAttributesCommandAttributes(betterproto.Message):
    search_attributes: v1common.SearchAttributes = betterproto.message_field(1)


@dataclass
class RecordMarkerCommandAttributes(betterproto.Message):
    marker_name: str = betterproto.string_field(1)
    details: Dict[str, v1common.Payloads] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    header: v1common.Header = betterproto.message_field(3)
    failure: v1failure.Failure = betterproto.message_field(4)


@dataclass
class ContinueAsNewWorkflowExecutionCommandAttributes(betterproto.Message):
    workflow_type: v1common.WorkflowType = betterproto.message_field(1)
    task_queue: v1taskqueue.TaskQueue = betterproto.message_field(2)
    input: v1common.Payloads = betterproto.message_field(3)
    # workflow_execution_timeout is omitted as it shouldn'be overridden from
    # within a workflow. Timeout of a single workflow run.
    workflow_run_timeout_seconds: int = betterproto.int32_field(4)
    # Timeout of a single workflow task.
    workflow_task_timeout_seconds: int = betterproto.int32_field(5)
    backoff_start_interval_in_seconds: int = betterproto.int32_field(6)
    retry_policy: v1common.RetryPolicy = betterproto.message_field(7)
    initiator: v1enums.ContinueAsNewInitiator = betterproto.enum_field(8)
    failure: v1failure.Failure = betterproto.message_field(9)
    last_completion_result: v1common.Payloads = betterproto.message_field(10)
    cron_schedule: str = betterproto.string_field(11)
    header: v1common.Header = betterproto.message_field(12)
    memo: v1common.Memo = betterproto.message_field(13)
    search_attributes: v1common.SearchAttributes = betterproto.message_field(14)


@dataclass
class StartChildWorkflowExecutionCommandAttributes(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    workflow_id: str = betterproto.string_field(2)
    workflow_type: v1common.WorkflowType = betterproto.message_field(3)
    task_queue: v1taskqueue.TaskQueue = betterproto.message_field(4)
    input: v1common.Payloads = betterproto.message_field(5)
    # Total workflow execution timeout including retries and continue as new.
    workflow_execution_timeout_seconds: int = betterproto.int32_field(6)
    # Timeout of a single workflow run.
    workflow_run_timeout_seconds: int = betterproto.int32_field(7)
    # Timeout of a single workflow task.
    workflow_task_timeout_seconds: int = betterproto.int32_field(8)
    # Default: PARENT_CLOSE_POLICY_TERMINATE.
    parent_close_policy: v1enums.ParentClosePolicy = betterproto.enum_field(9)
    control: str = betterproto.string_field(10)
    # Default: WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE.
    workflow_id_reuse_policy: v1enums.WorkflowIdReusePolicy = betterproto.enum_field(11)
    retry_policy: v1common.RetryPolicy = betterproto.message_field(12)
    cron_schedule: str = betterproto.string_field(13)
    header: v1common.Header = betterproto.message_field(14)
    memo: v1common.Memo = betterproto.message_field(15)
    search_attributes: v1common.SearchAttributes = betterproto.message_field(16)


@dataclass
class Command(betterproto.Message):
    command_type: v1enums.CommandType = betterproto.enum_field(1)
    schedule_activity_task_command_attributes: "ScheduleActivityTaskCommandAttributes" = betterproto.message_field(
        2, group="attributes"
    )
    start_timer_command_attributes: "StartTimerCommandAttributes" = betterproto.message_field(
        3, group="attributes"
    )
    complete_workflow_execution_command_attributes: "CompleteWorkflowExecutionCommandAttributes" = betterproto.message_field(
        4, group="attributes"
    )
    fail_workflow_execution_command_attributes: "FailWorkflowExecutionCommandAttributes" = betterproto.message_field(
        5, group="attributes"
    )
    request_cancel_activity_task_command_attributes: "RequestCancelActivityTaskCommandAttributes" = betterproto.message_field(
        6, group="attributes"
    )
    cancel_timer_command_attributes: "CancelTimerCommandAttributes" = betterproto.message_field(
        7, group="attributes"
    )
    cancel_workflow_execution_command_attributes: "CancelWorkflowExecutionCommandAttributes" = betterproto.message_field(
        8, group="attributes"
    )
    request_cancel_external_workflow_execution_command_attributes: "RequestCancelExternalWorkflowExecutionCommandAttributes" = betterproto.message_field(
        9, group="attributes"
    )
    record_marker_command_attributes: "RecordMarkerCommandAttributes" = betterproto.message_field(
        10, group="attributes"
    )
    continue_as_new_workflow_execution_command_attributes: "ContinueAsNewWorkflowExecutionCommandAttributes" = betterproto.message_field(
        11, group="attributes"
    )
    start_child_workflow_execution_command_attributes: "StartChildWorkflowExecutionCommandAttributes" = betterproto.message_field(
        12, group="attributes"
    )
    signal_external_workflow_execution_command_attributes: "SignalExternalWorkflowExecutionCommandAttributes" = betterproto.message_field(
        13, group="attributes"
    )
    upsert_workflow_search_attributes_command_attributes: "UpsertWorkflowSearchAttributesCommandAttributes" = betterproto.message_field(
        14, group="attributes"
    )