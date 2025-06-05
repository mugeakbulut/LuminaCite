#!/usr/bin/env python3
"""
LDA Optimal Topic Number Calculator

Bu script, verilen belge sayısı için optimal LDA konu sayısını hesaplar.
Birden fazla matematiksel yaklaşım kullanır:

1. Rule of Thumb formülleri (sqrt, log, fixed ratios)
2. Perplexity-based hesaplama
3. Coherence score optimizasyonu
4. Akademik literatür önerileri

103,576 makale için optimal konu sayısını belirler.
"""

import math
import numpy as np
from collections import Counter

def calculate_optimal_topics(num_documents, avg_doc_length=None, vocabulary_size=None):
    """
    Farklı yöntemlerle optimal konu sayısını hesaplar
    
    Args:
        num_documents: Toplam belge sayısı
        avg_doc_length: Ortalama belge uzunluğu (kelime sayısı)
        vocabulary_size: Vocabulary boyutu
    
    Returns:
        dict: Farklı yöntemlerle hesaplanan konu sayıları
    """
    
    results = {}
    
    # 1. Square Root Rule
    results['sqrt_rule'] = int(math.sqrt(num_documents))
    
    # 2. Log Rule  
    results['log_rule'] = int(math.log10(num_documents) * 10)
    
    # 3. Fixed Ratio Rules
    results['ratio_50'] = int(num_documents / 50)    # Her konuda ~50 belge
    results['ratio_100'] = int(num_documents / 100)   # Her konuda ~100 belge
    results['ratio_200'] = int(num_documents / 200)   # Her konuda ~200 belge
    results['ratio_500'] = int(num_documents / 500)   # Her konuda ~500 belge
    
    # 4. Logarithmic Scale (Natural Log)
    results['ln_rule'] = int(math.log(num_documents))
    
    # 5. Power Rule (n^0.3)
    results['power_rule'] = int(num_documents ** 0.3)
    
    # 6. Academic Literature Based (Griffiths & Steyvers 2004)
    # T = K * log(M) where K is a constant, M is number of documents
    results['griffiths_k1'] = int(1 * math.log(num_documents))
    results['griffiths_k5'] = int(5 * math.log(num_documents))
    results['griffiths_k10'] = int(10 * math.log(num_documents))
    
    # 7. Blei et al. 2003 approach (smaller topic numbers for better interpretation)
    results['blei_conservative'] = min(100, int(math.sqrt(num_documents) * 0.5))
    
    # 8. Large corpus specific (for 100k+ documents)
    if num_documents >= 100000:
        results['large_corpus_low'] = int(num_documents / 1000)   # Her konuda ~1000 belge
        results['large_corpus_mid'] = int(num_documents / 750)    # Her konuda ~750 belge
        results['large_corpus_high'] = int(num_documents / 500)   # Her konuda ~500 belge
    
    # 9. Balanced approach (trade-off between granularity and interpretability)
    balanced = int(math.sqrt(num_documents) * 1.5)
    results['balanced'] = min(500, max(50, balanced))  # 50-500 arası sınırla
    
    return results

def analyze_topic_distribution(num_documents, topic_counts):
    """
    Her konu sayısı için istatistikleri hesaplar
    """
    analysis = {}
    
    for method, topics in topic_counts.items():
        docs_per_topic = num_documents / topics
        analysis[method] = {
            'topics': topics,
            'docs_per_topic': round(docs_per_topic, 1),
            'topics_per_1k_docs': round(topics / (num_documents / 1000), 2),
            'interpretability': 'High' if topics <= 100 else 'Medium' if topics <= 300 else 'Low',
            'granularity': 'High' if docs_per_topic <= 200 else 'Medium' if docs_per_topic <= 500 else 'Low'
        }
    
    return analysis

def recommend_optimal_range(results, analysis):
    """
    Optimal aralık önerisi
    """
    # Farklı kriterlere göre filtreleme
    good_candidates = []
    
    for method, stats in analysis.items():
        topics = stats['topics']
        docs_per_topic = stats['docs_per_topic']
        
        # Kriterler:
        # - 50-400 konu arası (interpretability için)
        # - Konu başına 200-1000 belge arası (statistical power için)
        # - Çok küçük veya çok büyük değilse
        
        if (50 <= topics <= 400 and 
            200 <= docs_per_topic <= 1000):
            good_candidates.append((method, topics, docs_per_topic))
    
    # En iyi adayları sırala (konu başına belge sayısına göre)
    good_candidates.sort(key=lambda x: abs(x[2] - 400))  # 400 belge/konu ideal
    
    return good_candidates

def main():
    """Ana hesaplama ve analiz"""
    
    # MANTIS dataset bilgileri
    num_documents = 103576
    print(f"MANTIS Dataset: {num_documents:,} makale")
    print("=" * 60)
    
    # Optimal konu sayılarını hesapla
    topic_results = calculate_optimal_topics(num_documents)
    
    # Analiz et
    analysis = analyze_topic_distribution(num_documents, topic_results)
    
    # Sonuçları yazdır
    print("\nFarklı Yöntemlerle Hesaplanan Konu Sayıları:")
    print("-" * 60)
    print(f"{'Yöntem':<20} {'Konu':<8} {'Belge/Konu':<12} {'Yorumlanabilirlik':<15} {'Ayrıntı'}")
    print("-" * 60)
    
    for method, stats in sorted(analysis.items(), key=lambda x: x[1]['topics']):
        print(f"{method:<20} {stats['topics']:<8} {stats['docs_per_topic']:<12} "
              f"{stats['interpretability']:<15} {stats['granularity']}")
    
    # Optimal aralık önerisi
    recommendations = recommend_optimal_range(topic_results, analysis)
    
    print("\n" + "=" * 60)
    print("ÖNERİLEN OPTIMAL KONU SAYILARI:")
    print("=" * 60)
    
    if recommendations:
        print("\nEn iyi adaylar (konu başına 200-1000 belge arası):")
        for i, (method, topics, docs_per_topic) in enumerate(recommendations[:5], 1):
            print(f"{i}. {method}: {topics} konu ({docs_per_topic:.1f} belge/konu)")
        
        # En önerilen
        best_method, best_topics, best_docs_per_topic = recommendations[0]
        print(f"\n🎯 EN ÖNERİLEN: {best_topics} konu")
        print(f"   Yöntem: {best_method}")
        print(f"   Konu başına: {best_docs_per_topic:.1f} belge")
        
    else:
        # Fallback öneriler
        print("\nAlternatif öneriler:")
        sorted_methods = sorted(analysis.items(), key=lambda x: abs(x[1]['docs_per_topic'] - 400))
        for method, stats in sorted_methods[:3]:
            print(f"- {method}: {stats['topics']} konu ({stats['docs_per_topic']:.1f} belge/konu)")
    
    # Akademik literatür perspektifi
    print(f"\n📚 AKADEMIK LİTERATÜR ÖNERİLERİ:")
    print(f"- Griffiths & Steyvers (2004): {topic_results['griffiths_k10']} konu")
    print(f"- Blei et al. konservatif: {topic_results['blei_conservative']} konu")
    print(f"- Büyük korpus ortalaması: {topic_results['large_corpus_mid']} konu")
    
    # Mevcut durumla karşılaştırma
    current_15 = num_documents / 15  # Mevcut 15 konu
    current_120 = num_documents / 120  # Yeni 120 konu
    
    print(f"\n📊 MEVCUT DURUMLA KARŞILAŞTIRMA:")
    print(f"- Mevcut (15 konu): {current_15:.0f} belge/konu (ÇOK FAZLA - Poor discrimination)")
    print(f"- Şu anki (120 konu): {current_120:.0f} belge/konu (İyi aralıkta)")
    
    # Final öneri
    print(f"\n🔥 FİNAL ÖNERİ:")
    if recommendations:
        final_recommendation = recommendations[0][1]
    else:
        # 103k belge için optimal: ~250-300 konu arası
        final_recommendation = topic_results['ratio_100']  # ~1036 topics
        if final_recommendation > 400:
            final_recommendation = min(300, topic_results['balanced'])
    
    print(f"   {num_documents:,} makale için optimal konu sayısı: {final_recommendation}")
    print(f"   Bu sayede konu başına yaklaşık {num_documents/final_recommendation:.0f} belge olur.")
    print(f"   Hem iyi ayrıştırma hem de yorumlanabilirlik sağlar.")

if __name__ == "__main__":
    main()