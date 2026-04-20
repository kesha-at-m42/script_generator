extends SequenceEvent

func trigger() -> void:
	var parts = get_frac_shape(1)._parts
	var shaded_part = parts.filter(func(frac): return frac.is_shaded)[1]
	use_paint_tool(get_frac_shape_part(0, parts.find(shaded_part)))
