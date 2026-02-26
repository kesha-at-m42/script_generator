# Copyright Mission 42 Ventures, Inc. All rights reserved.
# Unauthorized copying, distribution, or use is prohibited.

class_name SequencePoolSchema extends Node

static var J := JSONSchema

# ============================================================================
# SEQUENCE POOL
# ============================================================================

static func create_schema() -> JSONSchema.BaseSchema:
	return J.object({
		"sequences": J.array(SequenceSchema.create_schema())
	}).keep_extra_fields_in("metadata").type(SequencePool)
