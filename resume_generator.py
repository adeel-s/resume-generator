import services.keyword_analyzer as keywordAnalyzer
import services.bullet_writer as bulletWriter

keywords = keywordAnalyzer.analyze()

bullets = bulletWriter.writeBullets(keywords)

print(bullets)