extends SequenceEvent

func trigger() -> void:
	use_write_tool(get_frac_shape()._parts.filter(func(frac): return frac.is_shaded)[1], "2")
