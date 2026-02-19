# Copyright Mission 42 Ventures, Inc. All rights reserved.
# Unauthorized copying, distribution, or use is prohibited.

class_name PoolSchema extends Node

static var J := JSONSchema

# ============================================================================
# POOL
# ============================================================================

static func create_schema() -> JSONSchema.BaseSchema:
	return J.object({
		"id": J.string(),
		"requested_count": J.integer(),
		"shuffle": J.boolean().optional(),
		"use_tiers": J.boolean().optional()
	}).type(PoolData)
