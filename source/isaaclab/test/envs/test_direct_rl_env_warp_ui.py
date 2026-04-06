# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from isaaclab_experimental.envs.direct_rl_env_warp import DirectRLEnvWarp

from isaaclab.envs.ui.base_env_window import BaseEnvWindow


def test_direct_rl_env_warp_ui_window_requires_gui():
    env = object.__new__(DirectRLEnvWarp)
    env.sim = type("Sim", (), {"has_gui": False})()
    env.cfg = type("Cfg", (), {"ui_window_class_type": object})()

    assert env._should_create_ui_window() is False


def test_direct_rl_env_warp_ui_window_created_when_gui_and_window_type_exist():
    env = object.__new__(DirectRLEnvWarp)
    env.sim = type("Sim", (), {"has_gui": True})()
    env.cfg = type("Cfg", (), {"ui_window_class_type": object})()

    assert env._should_create_ui_window() is True


def test_direct_rl_env_warp_ui_window_skipped_without_window_type():
    env = object.__new__(DirectRLEnvWarp)
    env.sim = type("Sim", (), {"has_gui": True})()
    env.cfg = type("Cfg", (), {"ui_window_class_type": None})()

    assert env._should_create_ui_window() is False


def test_base_env_window_destructor_tolerates_partial_initialization():
    window = object.__new__(BaseEnvWindow)
    window.__del__()
