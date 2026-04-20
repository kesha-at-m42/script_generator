extends SequenceEvent

func trigger() -> void:
	use_highlight_tool(get_frac_shape(1)._parts.filter(func(frac): return frac.is_shaded)[1], true)
