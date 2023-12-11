from scr.models.entities.attention_control import AttentionControl
from scr.models.model_attention_control import ModelAttentionControl

# insert test

#attention_control = AttentionControl("2021-09-01", "Juan Perez", "08:00:00", "17:00:00", True, True, "Si")
#ModelAttentionControl.insert_attention_control(attention_control)

#updated test

# attention_control = AttentionControl("2023-09-01", "Juan Perez Contreras", "09:00:00", "17:00:00", False, False, "Si", 22)
# ModelAttentionControl.update_attention_control(attention_control)

#delete test
ModelAttentionControl.delete_attention_control(22)