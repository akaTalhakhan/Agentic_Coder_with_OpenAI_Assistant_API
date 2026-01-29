"""
Enhanced AI Coding Companion Configuration
==========================================

This file contains all configuration settings for the Enhanced AI Coding Companion.
Modify these settings to customize the behavior and appearance of your application.
"""

import os
from typing import Dict, List, Any

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================

APP_CONFIG = {
    "title": "🚀 Enhanced AI Coding Companion",
    "subtitle": "Your Intelligent Programming Partner with Advanced Analytics",
    "version": "2.0.0",
    "author": "AI Coding Companion Team",
    "contact": "support@aicodingcompanion.com",
    "github_url": "https://github.com/your-username/enhanced-ai-coding-companion",
    "documentation_url": "https://docs.ai-coding-companion.com",
}

# =============================================================================
# STREAMLIT CONFIGURATION
# =============================================================================

STREAMLIT_CONFIG = {
    "page_title": APP_CONFIG["title"],
    "page_icon": "🚀",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "Get Help": APP_CONFIG["documentation_url"],
        "Report a bug": f"{APP_CONFIG['github_url']}/issues",
        "About": f"# {APP_CONFIG['title']} v{APP_CONFIG['version']}\n\nDeveloped by {APP_CONFIG['author']}",
    },
}

# =============================================================================
# AI MODEL CONFIGURATIONS
# =============================================================================

AI_MODELS = {
    "ChatGPT-4": {
        "api_name": "gpt-4",
        "max_tokens": 4000,
        "temperature": 0.3,
        "description": "Most advanced model with superior reasoning",
        "cost_per_token": 0.03,
        "capabilities": ["code_generation", "analysis", "refactoring", "documentation"],
    },
    "GPT-3.5-Turbo": {
        "api_name": "gpt-3.5-turbo",
        "max_tokens": 4000,
        "temperature": 0.3,
        "description": "Fast and efficient for most coding tasks",
        "cost_per_token": 0.002,
        "capabilities": ["code_generation", "analysis", "basic_refactoring"],
    },
    "Gemini Pro": {
        "api_name": "gemini-pro",
        "max_tokens": 4000,
        "temperature": 0.3,
        "description": "Google's advanced multimodal AI",
        "cost_per_token": 0.001,
        "capabilities": ["code_generation", "analysis", "multimodal"],
    },
    "Claude-3": {
        "api_name": "claude-3-sonnet",
        "max_tokens": 4000,
        "temperature": 0.3,
        "description": "Anthropic's safe and helpful AI",
        "cost_per_token": 0.015,
        "capabilities": ["code_generation", "analysis", "safety_focused"],
    },
}

# =============================================================================
# ANALYSIS FEATURES CONFIGURATION
# =============================================================================

ANALYSIS_FEATURES = {
    "security_scan": {
        "enabled": True,
        "severity_levels": ["High", "Medium", "Low"],
        "patterns": {
            "sql_injection": r'execute\s*\(\s*["\'].*%.*["\']',
            "hardcoded_password": r'password\s*=\s*["\'][^"\']+["\']',
            "eval_usage": r"\beval\s*\(",
            "insecure_random": r"random\.",
            "debug_mode": r"debug\s*=\s*True",
        },
    },
    "performance_analysis": {
        "enabled": True,
        "optimization_patterns": [
            "range_len_to_enumerate",
            "list_comprehension",
            "dict_get_method",
            "context_managers",
        ],
        "complexity_metrics": ["cyclomatic", "cognitive", "halstead"],
    },
    "code_quality": {
        "enabled": True,
        "metrics": [
            "readability",
            "maintainability",
            "documentation",
            "best_practices",
        ],
        "thresholds": {"excellent": 9, "good": 7, "fair": 5, "poor": 3},
    },
}

# =============================================================================
# TESTING CONFIGURATION
# =============================================================================

TESTING_CONFIG = {
    "frameworks": {
        "pytest": {
            "imports": ["pytest", "unittest.mock"],
            "decorators": ["@pytest.fixture", "@pytest.mark.parametrize"],
            "assertions": "assert",
        },
        "unittest": {
            "imports": ["unittest", "unittest.mock"],
            "base_class": "unittest.TestCase",
            "assertions": "self.assert",
        },
        "nose2": {
            "imports": ["nose2", "unittest"],
            "decorators": ["@nose2.tools.params"],
            "assertions": "assert",
        },
    },
    "coverage_targets": {"minimum": 70, "good": 80, "excellent": 90, "perfect": 100},
    "test_types": ["unit", "integration", "performance", "security"],
}

# =============================================================================
# VISUALIZATION SETTINGS
# =============================================================================

VISUALIZATION_CONFIG = {
    "color_schemes": {
        "default": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
        "pastel": ["#AED6F1", "#F9E79F", "#ABEBC6", "#F1948A", "#D7BDE2"],
        "corporate": ["#2C3E50", "#3498DB", "#E74C3C", "#F39C12", "#27AE60"],
    },
    "chart_height": 400,
    "font_family": "Arial, sans-serif",
    "background_color": "white",
    "grid_color": "#E5E5E5",
}

# =============================================================================
# LANGUAGE SUPPORT
# =============================================================================

SUPPORTED_LANGUAGES = {
    "Python": {
        "extensions": [".py", ".pyw"],
        "syntax_highlighting": "python",
        "complexity_analysis": True,
        "security_patterns": True,
    },
    "JavaScript": {
        "extensions": [".js", ".mjs"],
        "syntax_highlighting": "javascript",
        "complexity_analysis": True,
        "security_patterns": True,
    },
    "TypeScript": {
        "extensions": [".ts", ".tsx"],
        "syntax_highlighting": "typescript",
        "complexity_analysis": True,
        "security_patterns": True,
    },
    "Java": {
        "extensions": [".java"],
        "syntax_highlighting": "java",
        "complexity_analysis": True,
        "security_patterns": True,
    },
    "C++": {
        "extensions": [".cpp", ".cc", ".cxx"],
        "syntax_highlighting": "cpp",
        "complexity_analysis": True,
        "security_patterns": False,
    },
    "Go": {
        "extensions": [".go"],
        "syntax_highlighting": "go",
        "complexity_analysis": True,
        "security_patterns": True,
    },
    "Rust": {
        "extensions": [".rs"],
        "syntax_highlighting": "rust",
        "complexity_analysis": True,
        "security_patterns": True,
    },
}

# =============================================================================
# UI CUSTOMIZATION
# =============================================================================

UI_CONFIG = {
    "sidebar": {
        "width": 300,
        "default_collapsed": False,
        "sections": [
            "configuration",
            "quick_actions",
            "project_info",
            "export_options",
        ],
    },
    "main_tabs": [
        "💻 Code Editor",
        "📊 Analytics",
        "💬 AI Chat",
        "🔍 Analysis",
        "🧪 Testing",
        "📈 Visualization",
    ],
    "metrics_display": {
        "columns": 4,
        "show_deltas": True,
        "update_interval": 5,  # seconds
    },
    "code_editor": {
        "theme": "monokai",
        "font_size": 14,
        "line_numbers": True,
        "word_wrap": True,
        "auto_complete": True,
    },
}

# =============================================================================
# EXPORT AND INTEGRATION SETTINGS
# =============================================================================

EXPORT_CONFIG = {
    "formats": {
        "pdf": {"enabled": True, "template": "professional", "include_charts": True},
        "json": {"enabled": True, "pretty_print": True, "include_metadata": True},
        "markdown": {"enabled": True, "include_toc": True, "code_highlighting": True},
        "html": {"enabled": True, "responsive": True, "include_css": True},
    },
    "api_endpoints": {
        "base_url": "https://api.ai-coding-companion.com/v1",
        "timeout": 30,
        "retry_attempts": 3,
    },
}

# =============================================================================
# SECURITY AND PRIVACY SETTINGS
# =============================================================================

SECURITY_CONFIG = {
    "api_key_encryption": True,
    "local_processing": True,
    "data_retention": {
        "chat_history": 24,  # hours
        "analysis_results": 7,  # days
        "code_history": 30,  # days
    },
    "audit_logging": {"enabled": True, "log_level": "INFO", "retention_days": 90},
    "rate_limiting": {"requests_per_minute": 60, "requests_per_hour": 1000},
}

# =============================================================================
# PERFORMANCE SETTINGS
# =============================================================================

PERFORMANCE_CONFIG = {
    "caching": {
        "enabled": True,
        "ttl": 3600,  # seconds
        "max_size": 100,  # MB
    },
    "parallel_processing": {"enabled": True, "max_workers": 4},
    "optimization": {"lazy_loading": True, "compression": True, "minification": True},
}

# =============================================================================
# DEVELOPMENT AND DEBUG SETTINGS
# =============================================================================

DEBUG_CONFIG = {
    "enabled": os.getenv("DEBUG", "False").lower() == "true",
    "log_level": "DEBUG" if os.getenv("DEBUG") else "INFO",
    "show_performance_metrics": True,
    "mock_ai_responses": os.getenv("MOCK_AI", "False").lower() == "true",
    "verbose_logging": True,
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def get_config(section: str = None) -> Dict[str, Any]:
    """Get configuration for a specific section or all configs."""
    configs = {
        "app": APP_CONFIG,
        "streamlit": STREAMLIT_CONFIG,
        "ai_models": AI_MODELS,
        "analysis": ANALYSIS_FEATURES,
        "testing": TESTING_CONFIG,
        "visualization": VISUALIZATION_CONFIG,
        "languages": SUPPORTED_LANGUAGES,
        "ui": UI_CONFIG,
        "export": EXPORT_CONFIG,
        "security": SECURITY_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "debug": DEBUG_CONFIG,
    }

    if section:
        return configs.get(section, {})
    return configs


def validate_config() -> List[str]:
    """Validate configuration settings and return any issues."""
    issues = []

    # Check required environment variables
    required_env_vars = ["OPENAI_API_KEY", "GOOGLE_API_KEY"]
    for var in required_env_vars:
        if not os.getenv(var):
            issues.append(f"Missing environment variable: {var}")

    # Validate model configurations
    for model_name, config in AI_MODELS.items():
        if "api_name" not in config:
            issues.append(f"Missing api_name for model: {model_name}")

    return issues


def apply_custom_config(custom_config: Dict[str, Any]) -> None:
    """Apply custom configuration overrides."""
    global APP_CONFIG, STREAMLIT_CONFIG, AI_MODELS

    # Update configurations with custom values
    for section, values in custom_config.items():
        if section == "app":
            APP_CONFIG.update(values)
        elif section == "streamlit":
            STREAMLIT_CONFIG.update(values)
        elif section == "ai_models":
            AI_MODELS.update(values)
        # Add more sections as needed


# =============================================================================
# INITIALIZATION
# =============================================================================


def initialize_config():
    """Initialize configuration and validate settings."""
    issues = validate_config()
    if issues and not DEBUG_CONFIG["enabled"]:
        raise ValueError(f"Configuration issues found: {', '.join(issues)}")

    return get_config()


# Export main configuration
CONFIG = initialize_config()
