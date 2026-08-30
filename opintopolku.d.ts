export interface RawEducation {
  jakolinkki: Jakolinkki
  henkilö: Henkilö
  opiskeluoikeudet: Opiskeluoikeudet[]
}

export interface Jakolinkki {
  voimassaAsti: string
}

export interface Henkilö {
  oid: string
  syntymäaika: string
  etunimet: string
  kutsumanimi: string
  sukunimi: string
  äidinkieli: Äidinkieli
}

export interface Äidinkieli {
  koodiarvo: string
  nimi: Nimi
  lyhytNimi: LyhytNimi
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi {
  fi: string
  sv: string
  en: string
}

export interface Opiskeluoikeudet {
  oid: string
  versionumero: number
  aikaleima: string
  lähdejärjestelmänId: LähdejärjestelmäId
  oppilaitos: Oppilaitos
  koulutustoimija: Koulutustoimija
  arvioituPäättymispäivä: string
  tila: Tila
  lisätiedot: Lisätiedot
  suoritukset: Suoritukset[]
  tyyppi: Tyyppi4
  oppimääräSuoritettu: boolean
  alkamispäivä: string
}

export interface LähdejärjestelmäId {
  id: string
  lähdejärjestelmä: LähdeJärjestelmä
}

export interface LähdeJärjestelmä {
  koodiarvo: string
  nimi: Nimi2
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi2 {
  fi: string
}

export interface Oppilaitos {
  oid: string
  oppilaitosnumero: Oppilaitosnumero
  nimi: Nimi4
  kotipaikka: Kotipaikka
}

export interface Oppilaitosnumero {
  koodiarvo: string
  nimi: Nimi3
  lyhytNimi: LyhytNimi2
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi3 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi2 {
  fi: string
  sv: string
  en: string
}

export interface Nimi4 {
  fi: string
  sv: string
  en: string
}

export interface Kotipaikka {
  koodiarvo: string
  nimi: Nimi5
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi5 {
  fi: string
  sv: string
}

export interface Koulutustoimija {
  oid: string
  nimi: Nimi6
  yTunnus: string
  kotipaikka: Kotipaikka2
}

export interface Nimi6 {
  fi: string
  sv: string
  en: string
}

export interface Kotipaikka2 {
  koodiarvo: string
  nimi: Nimi7
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi7 {
  fi: string
  sv: string
}

export interface Tila {
  opiskeluoikeusjaksot: Opiskeluoikeusjaksot[]
}

export interface Opiskeluoikeusjaksot {
  alku: string
  tila: Tila2
  opintojenRahoitus: OpintojenRahoitus
}

export interface Tila2 {
  koodiarvo: string
  nimi: Nimi8
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi8 {
  fi: string
  sv: string
  en: string
}

export interface OpintojenRahoitus {
  koodiarvo: string
  nimi: Nimi9
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi9 {
  fi: string
  sv: string
  en: string
}

export interface Lisätiedot {
  pidennettyPäättymispäivä: boolean
  ulkomainenVaihtoopiskelija: boolean
  maksuttomuus: Maksuttomuu[]
}

export interface Maksuttomuu {
  alku: string
  maksuton: boolean
}

export interface Suoritukset {
  koulutusmoduuli: Koulutusmoduuli
  oppimäärä: Oppimr
  toimipiste: Toimipiste
  suoritettuErityisenäTutkintona: boolean
  suorituskieli: Suorituskieli
  osasuoritukset: Osasuoritukset[]
  tyyppi: Tyyppi3
  ryhmä: string
}

export interface Koulutusmoduuli {
  tunniste: Tunniste
  perusteenDiaarinumero: string
  koulutustyyppi: Koulutustyyppi
}

export interface Tunniste {
  koodiarvo: string
  nimi: Nimi10
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi10 {
  fi: string
  sv: string
  en: string
}

export interface Koulutustyyppi {
  koodiarvo: string
  nimi: Nimi11
  lyhytNimi: LyhytNimi3
  koodistoUri: string
}

export interface Nimi11 {
  fi: string
  sv: string
}

export interface LyhytNimi3 {
  fi: string
  sv: string
}

export interface Oppimäärä {
  koodiarvo: string
  nimi: Nimi12
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi12 {
  fi: string
  sv: string
  en: string
}

export interface Toimipiste {
  oid: string
  oppilaitosnumero: Oppilaitosnumero2
  nimi: Nimi14
  kotipaikka: Kotipaikka3
}

export interface Oppilaitosnumero2 {
  koodiarvo: string
  nimi: Nimi13
  lyhytNimi: LyhytNimi4
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi13 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi4 {
  fi: string
  sv: string
  en: string
}

export interface Nimi14 {
  fi: string
  sv: string
  en: string
}

export interface Kotipaikka3 {
  koodiarvo: string
  nimi: Nimi15
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi15 {
  fi: string
  sv: string
}

export interface Suorituskieli {
  koodiarvo: string
  nimi: Nimi16
  lyhytNimi: LyhytNimi5
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi16 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi5 {
  fi: string
  sv: string
  en: string
}

export interface Osasuoritukset {
  koulutusmoduuli: Koulutusmoduuli2
  suoritettuErityisenäTutkintona: boolean
  osasuoritukset: Osasuoritukset2[]
  tyyppi: Tyyppi2
  arviointi?: Arviointi2[]
}

export interface Koulutusmoduuli2 {
  tunniste: Tunniste2
  kieli?: Kieli
  pakollinen: boolean
  laajuus: Laajuus
  oppimäärä?: Oppimäärä2
  kuvaus?: Kuvaus
}

export interface Tunniste2 {
  koodiarvo: string
  nimi: Nimi17
  lyhytNimi?: LyhytNimi6
  koodistoUri?: string
  koodistoVersio?: number
}

export interface Nimi17 {
  fi: string
  sv?: string
  en: string
}

export interface LyhytNimi6 {
  fi: string
  sv?: string
}

export interface Kieli {
  koodiarvo: string
  nimi: Nimi18
  koodistoUri: string
  koodistoVersio: number
  lyhytNimi?: LyhytNimi7
}

export interface Nimi18 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi7 {
  fi: string
  sv: string
  en: string
}

export interface Laajuus {
  arvo: number
  yksikkö: Yksikk
}

export interface Yksikk {
  koodiarvo: string
  nimi: Nimi19
  lyhytNimi: LyhytNimi8
  koodistoUri: string
}

export interface Nimi19 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi8 {
  fi: string
  sv: string
  en: string
}

export interface Oppimäärä2 {
  koodiarvo: string
  nimi: Nimi20
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi20 {
  fi: string
  sv: string
  en: string
}

export interface Kuvaus {
  fi: string
}

export interface Osasuoritukset2 {
  koulutusmoduuli: Koulutusmoduuli3
  arviointi: Arviointi[]
  tyyppi: Tyyppi
}

export interface Koulutusmoduuli3 {
  tunniste: Tunniste3
  laajuus: Laajuus2
  pakollinen: boolean
  kieli?: Kieli2
  kuvaus?: Kuvaus2
}

export interface Tunniste3 {
  koodiarvo: string
  nimi: Nimi21
  koodistoUri?: string
  koodistoVersio?: number
}

export interface Nimi21 {
  fi: string
  sv?: string
  en: string
}

export interface Laajuus2 {
  arvo: number
  yksikkö: Yksikkö2
}

export interface Yksikkö2 {
  koodiarvo: string
  nimi: Nimi22
  lyhytNimi: LyhytNimi9
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi22 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi9 {
  fi: string
  sv: string
  en: string
}

export interface Kieli2 {
  koodiarvo: string
  nimi: Nimi23
  lyhytNimi: LyhytNimi10
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi23 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi10 {
  fi: string
  sv: string
  en: string
}

export interface Kuvaus2 {
  fi: string
}

export interface Arviointi {
  arvosana: Arvosana
  päivä: string
  hyväksytty: boolean
}

export interface Arvosana {
  koodiarvo: string
  nimi: Nimi24
  lyhytNimi: LyhytNimi11
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi24 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi11 {
  fi: string
}

export interface Tyyppi {
  koodiarvo: string
  nimi: Nimi25
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi25 {
  fi: string
  sv: string
  en: string
}

export interface Tyyppi2 {
  koodiarvo: string
  nimi: Nimi26
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi26 {
  fi: string
  sv: string
  en: string
}

export interface Arviointi2 {
  arvosana: Arvosana2
  hyväksytty: boolean
}

export interface Arvosana2 {
  koodiarvo: string
  nimi: Nimi27
  lyhytNimi: LyhytNimi12
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi27 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi12 {
  fi: string
}

export interface Tyyppi3 {
  koodiarvo: string
  nimi: Nimi28
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi28 {
  fi: string
  sv: string
  en: string
}

export interface Tyyppi4 {
  koodiarvo: string
  nimi: Nimi29
  lyhytNimi: LyhytNimi13
  koodistoUri: string
  koodistoVersio: number
}

export interface Nimi29 {
  fi: string
  sv: string
  en: string
}

export interface LyhytNimi13 {
  fi: string
}
