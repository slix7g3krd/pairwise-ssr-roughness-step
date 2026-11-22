import pytest
import render.ssr_roughness_step as mod

CASES = [
    ("step_by_roughness", (0.3, 0.7)),
    ("ray_jitter", (1, 2)),
    ("probe_fallback", (1, 2)),
    ("metal_smear", (1, 2)),
    ("coarse_surface", (1, 2)),
    ("march_budget", (64, 32)),
    ("thickness_test", (0.1, 0.2)),
    ("screen_edge", (1, 2)),
    ("color_leak", (1, 2)),
    ("roughness_lod", (1, 2)),
    ("hit_confirm", (1, 2)),
    ("ray_reuse", (1, 2)),
    ("denoise_reflection", (1, 2)),
    ("energy_scale", (0.5, 0.2)),
    ("validation", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
