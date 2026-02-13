#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing veo..."

# Install Python dependencies
if command -v uv &>/dev/null; then
    (cd "$SCRIPT_DIR" && uv sync)
else
    echo "Error: uv is required. Install it: https://docs.astral.sh/uv/"
    exit 1
fi

# Install CLI wrapper to ~/bin
mkdir -p "$HOME/bin"
cat > "$HOME/bin/veo" <<EOF
#!/usr/bin/env bash
exec uv run --project "$SCRIPT_DIR" veo "\$@"
EOF
chmod +x "$HOME/bin/veo"
echo "  Installed ~/bin/veo"

# Install Claude Code skills
for skill_dir in "$SCRIPT_DIR"/skills/*/; do
    skill_name="$(basename "$skill_dir")"
    mkdir -p "$HOME/.claude/skills/$skill_name"
    ln -sf "$skill_dir/SKILL.md" "$HOME/.claude/skills/$skill_name/SKILL.md"
    echo "  Installed skill: $skill_name"
done

echo ""
echo "Done! Make sure:"
echo "  1. ~/bin is in your PATH"
echo "  2. GEMINI_API_KEY is set in your environment"
echo ""
echo "Test it: veo models"
