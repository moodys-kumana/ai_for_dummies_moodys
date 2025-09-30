#!/usr/bin/env python3
"""
🔍 AI 4 DUMMIES - Deployment Readiness Checker
Verifica que todos los archivos estén listos para deployment en Streamlit Cloud
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Verifica si un archivo existe y muestra el resultado"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_file_content(filepath, required_content, description):
    """Verifica si un archivo contiene el contenido requerido"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if required_content in content:
                print(f"✅ {description}: Content OK")
                return True
            else:
                print(f"⚠️  {description}: Missing required content")
                return False
    except:
        print(f"❌ {description}: Cannot read file")
        return False

def main():
    """Función principal de verificación"""
    print("🚀 AI 4 DUMMIES - Deployment Readiness Check")
    print("=" * 50)
    
    all_good = True
    
    # Verificar archivos principales
    print("\n📁 Checking Core Files...")
    files_to_check = [
        ("ai_4_dummies_game.py", "Main Streamlit App"),
        ("requirements.txt", "Dependencies File"),
        ("README_DEPLOYMENT.md", "Documentation"),
        ("DEPLOYMENT_GUIDE.md", "Deployment Instructions"),
        (".streamlit/config.toml", "Streamlit Configuration")
    ]
    
    for filepath, desc in files_to_check:
        if not check_file_exists(filepath, desc):
            all_good = False
    
    # Verificar contenido específico
    print("\n🔍 Checking File Contents...")
    
    # Verificar requirements.txt
    if os.path.exists("requirements.txt"):
        required_deps = ["streamlit", "pandas", "numpy", "plotly"]
        for dep in required_deps:
            if not check_file_content("requirements.txt", dep, f"Dependency: {dep}"):
                all_good = False
    
    # Verificar main function en la app
    if os.path.exists("ai_4_dummies_game.py"):
        if not check_file_content("ai_4_dummies_game.py", 'if __name__ == "__main__":', "Main function check"):
            all_good = False
    
    # Verificar imports críticos
    critical_imports = ["streamlit", "pandas", "random", "time"]
    for imp in critical_imports:
        if not check_file_content("ai_4_dummies_game.py", f"import {imp}", f"Import: {imp}"):
            all_good = False
    
    # Resultados finales
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 DEPLOYMENT READY!")
        print("✅ All files and dependencies are properly configured")
        print("✅ Ready to push to GitHub and deploy to Streamlit Cloud")
        print("\n🚀 Next Steps:")
        print("1. Push code to GitHub: git push origin main")
        print("2. Go to https://share.streamlit.io/")
        print("3. Deploy your app!")
        print("4. Share URL: https://your-app-name.streamlit.app")
    else:
        print("❌ DEPLOYMENT NOT READY")
        print("⚠️  Please fix the issues above before deploying")
        print("📖 Check DEPLOYMENT_GUIDE.md for detailed instructions")
    
    print("\n💼 Repository: https://github.com/moodys-kumana/ai_for_dummies_moodys")
    print("📚 Streamlit Cloud: https://share.streamlit.io/")

if __name__ == "__main__":
    main()
